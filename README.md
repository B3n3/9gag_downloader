9gag Post Downloader
=======================

**These two scripts allows you to download posts from 9gag.com.**

GIFs will be stored as mp4.\
The caption of the posts will be used as filenames.

Requirements:
-------------

For [9gagDownloader.py](9gagDownloader.py) you need the following:
* [Python 3.x](https://www.python.org/downloads/)
* `requests` library\
Simply run `pip install requests` after installing Python 3.x or by running `pip install < requirements.txt`.

For [9gagCollector.js](9gagCollector.js) and [9gagExtractor.js](9gagExtractor.js) you only need:
* Google Chrome or Firefox


How to run it:
--------------

### Run the 9GAG-Extractor
First of all we have to collect a list of all posts which shall be downloaded later.\
This is done by opening the Browser Console (press *F12*) on the page where you want to download the posts.\
This script will only download posts which have been loaded(!). \
You can see which posts have been collected so far in the console. \
After you executed the script make sure that you scroll all the way down.

*Note, the script will check for new posts on the screen every 0.5 seconds.*

------------ 


![Extractor1](images/extractor1.png)

Copy and paste the complete code from [9gagCollector.js](9gagCollector.js) into the browser console and press Enter.
This will start collecting posts available on the screen. \
You can see which posts are captured in the console log.

![Extractor1.1](images/extractor1_1.png)


Once you are done with scrolling and no new posts are collected anymore, you can initiate the download by copy and pasting the code from [9gagExtractor.js](9gagExtractor.js) into the console.
This will start the download of a CSV file containing all the information needed for later.

![Extractor2](images/extractor2.png)
   
   
### Run the 9GAG-Downloader
Now that you have the CSV in place, fire up a console and run the [9gagDownloader.py](9gagDownloader.py) script like this:\
`python 9gagDownloader.py myExportFile.csv outputDirectory`

![Downloader1](images/downloader1.png)

You can now see how the script goes through all the posts and store them into the `outputDirectory`.

![Downloader2](images/downloader2.png)



Hints:
======

You can try the [example.csv](example.csv) file, if you just want to check whether or not your Python setup works:\
`python 9gagDownloader.py example.csv outputDirectory`