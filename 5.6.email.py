import smtplib
from email.mime.text import MIMEText

with open('mail') as file:
    key = file.read()
    keys = key.split(',')
    username = keys[0].strip()+'@gmail.com'
    password = keys[1].strip()

msg = MIMEText("The body of the email is here")
msg['Subject'] = "An Email Alert"
msg['From'] = username
msg['To'] = # to

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