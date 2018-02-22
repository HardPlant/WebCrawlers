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
cur.execute("USE wikipedia")

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    if links:
        return dict(zip(links, [{}]*len(links)))

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree: # 링크가 발견되지 않았음
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+" FOUND!")
        raise SolutionFound("PAGE: "+str(currentPageId))
    
    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        
        except SolutionFound as e:
            print(e.message)
            raise SolutionFound("PAGE: "+ str(currentPageId))
    return linkTree

try:
    searchDepth(134951, 1, {}, 4)
    print("No solution found")
except SolutionFound as e:
    print(e.message)


