from urllib.request import urlopen, HTTPError, Request
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

random.seed(datetime.datetime.now())

def getLinks(link):    
    html = urlopen('https://en.wikipedia.org'+link) # link는 /wiki/~ 형태로 반환된다.
    bsObj = BeautifulSoup(html, "html.parser")

    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="
    historyUrl += pageUrl + "&action=history"
    print("History URL is :" + historyUrl)
    
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()

    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    
    return addressList


def getCountry(ipAddress):
    request = Request("http://freegeoip.net/json/"+ipAddress,\
        headers={\
        'Upgrade-Insecure-Requests':'1',\
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',\
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',\
        })
    try:
        response = urlopen(request).read().decode('utf-8')
    except HTTPError:
        return None
    
    responseJson = json.loads(response)

    return responseJson.get('country_code')


links = getLinks("/wiki/Python_(programming_language)")
print(links)

while len(links) > 0:
    for link in links:
        print("--------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+ "is from "+country)
        
    newLink = links[random.randint(0, len(links) -1)].attrs['href']
    links = getLinks(newLink)