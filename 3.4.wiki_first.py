from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''
위키질하는 머신이다. 위케백과 메인 페이지부터 bodyContent에 있는 /wiki/링크들을 찾아 아무 링크에나 들어간다.
'''

pages = set()

def getLinks(link):
    global pages
    html = urlopen('https://en.wikipedia.org'+link) # link는 /wiki/~ 형태로 반환된다.
    bsObj = BeautifulSoup(html, "html.parser")

    print(bsObj.h1.get_text())
    print(bsObj.find("div",{'id':'mw-content-text'}).findAll("p")[0])
    print(bsObj.find("li", {'id':'ca-edit'}).find("span").find("a"))

    for link in bsObj.find("div",{'id':'bodyContent'}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
    
#url = '/wiki/Kevin_Bacon'
links = getLinks('')