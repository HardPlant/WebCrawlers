from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
URL을 이용해 pythonscraping.com에서 로고를 내려받아 logo.jpg라는 이름으로 저장한다.
'''

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a", {"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")


