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