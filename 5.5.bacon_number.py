from bs4 import BeautifulSoup
import re
import pymysql
from urllib.request import urlopen

with open('mysql') as file:
    key = file.read()
    keys = key.split(',')
    ip = keys[0].strip()
    user = keys[1].strip()
    password = keys[2].strip()

conn = pymysql.connect(host=ip, user=user,passwd=password, db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute("USE wikipedia")

'''
url에서 페이지를 가져와, 그 페이지의 첫번째에서 링크가 있는지 확인한다.
'''
def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()

    cur.execute("SELECT * FROM links WHERE fromPageId = %s", (int((page[0]))))
    if cur.rowcount == 0:
        return False
    return True

'''
페이지 리스트에서 url을 검색해 하나를 불러온다. 없으면 삽입한다.
'''

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES(%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

'''
확인된 링크를 테이블에 삽입한다.
'''
def insertLink(fromPageId, toPageId):
    cur.execute(
        "SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s",
        (int(fromPageId), int(toPageId))
    )
    if cur.rowcount == 0:
        cur.execute(
            "INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)",
            (int(fromPageId), int(toPageId))
        )
    conn.commit()

def getLinks(pageUrl, recursionLevel):
    if recursionLevel > 4:
        return
    
    pageId = insertPageIfNotExists(pageUrl)
    
    html = urlopen('https://en.wikipedia.org'+pageUrl) # link는 /wiki/~ 형태로 반환된다.
    bsObj = BeautifulSoup(html, "html.parser")

    for link in bsObj.findAll("a", href=re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel + 1)
        else:
            print("Skipping: "+str(link.attrs['href']+" found on "+pageUrl))

try:
    getLinks("/wiki/Kevin_Bacon", 0)
finally:
    cur.close()
    conn.close()
