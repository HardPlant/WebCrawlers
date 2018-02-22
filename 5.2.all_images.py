import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"


def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://")
        url = source
    elif source.startswith("www."):
        url = "http://"+source[4]
    else:
        url = baseUrl + '/' + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    
    directory = os.path.dirname(path)

    if not os.path.exist(directory):
        os.makedirs(directory)
    
    return path

