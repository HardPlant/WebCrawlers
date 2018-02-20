from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")


for link in bsObj.find("div",{'id':'bodyContent'}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# 위키백과의 주요 내용은 bodyContent 클래스 내에 있다.
# URL에는 세미콜론이 없다.
# URL은 /wiki/로 시작된다.

'''
다음과 같은 함수를 만들자.
1. getLinks 함수 : /wiki/article_name 형태인 항목 URL 전체를 반환하는 함수
2. getLinks()로 받은 목록 중 임의 항목을 선택해 다시 호출하는 항목
'''