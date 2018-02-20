from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    # /로 시작하는 링크를 모두 찾는다
    for link in bsObj.findAll('a', href=re.compile('^(/|.^'+includeUrl+')'):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith('/'):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # http, www로 시작하는 링크를 찾으며, 현재 URL은 포함하지 않는다.
    for link in bsObj.findAll('a', href=re.compile('^(http|www)(?!'+excludeUrl+').)*$'):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
    
    return externalLinks

def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme + '://' + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLinks(internalLinks[random,randint(0, len(internalLinks)-1)])
    
    else:
        return externalLinks[random,randint(0, len(internalLinks)-1]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print("Random external link is :" + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")