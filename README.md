9gag Profile Downloader
=======================

This script allows you to download a whole profile form 9gag.com with a given URL.

GIFs will be stored as mp4.
The caption of the posts will be used as filenames.

You can run the script like this:
```python 9gag.py http://9gag.com/u/YourFancyProfile downloadFolder```


Hints:
======

Remember that you can only download publicly available posts.
This means if you want to download eg. your upvotes, but your upvotes are *private*, the script will not be able to see them.
A simple solution would be to temporarily set them to *public*.

9GAG restricts the requests per minute, this is why I had to add a delay inbetween loading more posts.


Requirements:
=============

* requests (available via pip install)
* io
* sys
* os
* time


Known issues:
=============

The error handling could be improved further.
