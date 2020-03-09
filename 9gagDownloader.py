__author__ = "Benedikt Wedenik"
__license__ = "WTFPL"
__maintainer__ = "Benedikt Wedenik"
__email__ = "benedikt.wedenik@gmail.com"

import requests
import re
import io
import sys
import os

VALID_CHARS = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " export.csv download_directory")
    sys.exit(1)

CSV_FILE = sys.argv[1]
DW_DIR = sys.argv[2]
if not os.path.exists(DW_DIR):
    os.mkdir(DW_DIR)


def sanitize_filename(name):
    """
    Sanitizes a given filename to contain only valid chars based on the constant `VALID_CHARS`
    :param name: filename to be sanitized
    :return: string, sanitized filename
    """

    return ''.join(c for c in name if c in VALID_CHARS)


def download_file(url, name, extension):
    """
    Downloads a file based on a url and stores it under a given filename + file-extension
    :param url: string, e.g. https://9gag.com/imgxy.jpg
    :param name: string, is used as filename on the filesystem
    :param extension: string, file extension
    :return:
    """

    print("Downloading " + url)
    dw = requests.get(url)
    if dw.status_code == requests.codes.ok:
        name = sanitize_filename(name)
        path = DW_DIR + "/" + name + "." + extension

        # In case the file already exists, append a number and store it
        i = 1
        while True:
            if os.path.exists(path):
                path = DW_DIR + "/" + name + "_" + str(i) + "." + extension
                i = i + 1
            else:
                break

        print("Storing in " + path)
        binary = io.BytesIO(dw.content)
        with open(path, 'wb') as media:
            media.write(binary.read())


print("Grab a Snickers, we're about to get started...\n\n")

# Get file extension from the URL in the CSV
file_extension_regex = re.compile(r'.+\.(.+$)')

with open(CSV_FILE, 'r') as csv:
    for line in csv:
        content = line.split(',')
        filename = content[0].strip()
        url = content[1].strip()
        ext = file_extension_regex.search(url).group(1).strip()

        # Apparently it is sufficient to change the file-extension from webp to jpg,
        # for the gallery to correctly display it.
        if ext == 'webp':
            ext = 'jpg'
        try:
            download_file(url, filename, ext)
        except:
            print("ERROR while downloading this url " + url + " into this filename: " + filename + "." + ext)
            pass

# We're done
print("\nFinished! Go ahead now and check your " + DW_DIR + " folder full of fun :)\n\n")
banana = """
               ".           ,#  
               \ `-._____,-'=/
            ____`._ ----- _,'_____
                   `-----'
"""
print(banana)
print("PS: Banana for scale.")
