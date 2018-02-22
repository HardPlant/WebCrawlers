import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

with open('mail') as file:
    key = file.read()
    keys = key.split(',')
    username = keys[0].strip()+'@gmail.com'
    password = keys[1].strip()

def send_mail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = # To

    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.ehlo()
        s.starttls()
        s.login(username, password)
        s.send_message(msg)
        s.quit()
        print("Successed!")
    except Exception as e:
        print("Failed", e)

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3000)

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com/"))
send_mail("It's Christmas!"
,"According to http://itischristmas.com, it is Christmas!")