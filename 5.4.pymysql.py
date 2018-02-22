from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

with open('mysql') as file:
    key = file.read()
    keys = key.split(',')
    ip = keys[0].strip()
    user = keys[1].strip()
    password = keys[2].strip()

conn = pymysql.connect(host=ip, user=user,passwd=password, db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute(
        "INSERT INTO pages (title, content) VALUES (\"%s\",\"%s\")"
        , (title,content)
    )
    cur.connection.commit()

def getLinks(link):
    html = urlopen('https://en.wikipedia.org'+link) # link는 /wiki/~ 형태로 반환된다.
    bsObj = BeautifulSoup(html, "html.parser")

    title = bsObj.find("h1").find("span").get_text()
    content = bsOjb.find("div", {"id"L"mw-content-text"}).find("p").get_text()

    store(title,content)
    return bsObj.find("div",{'id':'bodyContent'}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))
    

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) -1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

finally:
    cur.close()
    conn.close()