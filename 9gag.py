__author__ = "Benedikt Wedenik"
__license__ = "WTFPL"
__maintainer__ = "Benedikt Wedenik"
__email__ = "benedikt.wedenik@gmail.com"


import requests
import re
import io
import sys
import os
import time

VALID_CHARS = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
URL_PREFIX = 'http://9gag.com'

if len(sys.argv) < 3:
    print "Usage: ", sys.argv[0], "url_to_download download_directory"
    sys.exit(1)

URL = sys.argv[1]
DW_DIR = sys.argv[2]
if not os.path.exists(DW_DIR):
    os.mkdir(DW_DIR)

#regex
re_item = re.compile(r'data-entry-url="(.*?)"')
re_mp4 = re.compile(r'data-mp4="(.*?)"')
re_img = re.compile(r'data-img="(.*?)"')
re_title = re.compile(r'<title>(.*?) - 9GAG</title>')
re_more_posts = re.compile(r'<a class="btn badge-load-more-post" href="(.*?)%.*?"')

def sanitize_filename(name):
    return ''.join(c for c in name if c in VALID_CHARS)

def download_file(url, name, extension):
    dw = requests.get(url)
    if dw.status_code == requests.codes.ok:
        name = sanitize_filename(name)
        path = DW_DIR + "/" + name + "." + extension
        i = 1
        while True:
            if os.path.exists(path):
                path = DW_DIR + "/" + name + "_" + str(i) + "." + extension
                i = i + 1
            else:
                break
        print "Downloading " + url + "   " + path

        binary = io.BytesIO(dw.content)
        img = open(path, 'w')
        img.write(binary.read())
        img.close()

def unify_to_single_line_and_close_request(req):
    page = ""
    for line in req:
        page = page + line.strip().replace('\n', '')
    req.close()
    return page

def go_to_item_page(url):
    r = requests.get(url)
    if r.status_code != requests.codes.ok:
        print "Invalid URL: " + url
        sys.exit(1)
    page = unify_to_single_line_and_close_request(r)
    res = re_title.search(page)
    if res:
        name = res.group(1)
        res = re_mp4.search(page)
        #if it is a GIF, download it as mp4, else just the image
        if res:
            download_file(res.group(1), name, "mp4")
        else:
            res = re_img.search(page)
            if res:
                download_file(res.group(1), name, "jpg")

#go through all posts and load more if necessary
while True:
    r = requests.get(URL)
    if r.status_code != requests.codes.ok:
        print "Invalid URL: " + URL
        sys.exit(1)

    page = unify_to_single_line_and_close_request(r)
    for match in re_item.finditer(page):
        go_to_item_page(match.group(1))

    res = re_more_posts.search(page)
    if res:
        nextUrl = URL_PREFIX + res.group(1)
        print "\nLoading more posts! Next URL " + nextUrl + "\n"
        URL = nextUrl
    else:
        break

    #sleep for 5 seconds to not exceed the max number of requests
    #9GAG somehow restricted too many requests
    time.sleep(5)

print "\nFinished!!!"

