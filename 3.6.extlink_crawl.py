from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

allExtLinks = set()
allIntLinks = set()


def getInternalLinks(bsObj, includeUrl): 
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    # /로 시작하는 링크를 모두 찾는다
    for link in bsObj.findAll('a', href=re.compile("^(/|.^"+includeUrl+")")):
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
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
    
    return externalLinks

def splitAddress(domain):
    return domain.split(',')

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, splitAddress(domain)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(domain)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    
    for link in internalLinks:
        if link == '/':
            link = domain
        elif link[0:2] == '//':
            link = "http:" + domain + link
        elif link[0:1] == '/':
            link = domain + link
        elif link[0:3] == ":///":
            link = domain + link[1:]

    if link not in allIntLinks:
        print("About to get link: " + link)
        allIntLinks.add(link)
        getAllExternalLinks(link)

domain = "http://oreilly.com"
getAllExternalLinks(domain)
