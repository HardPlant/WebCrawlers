import smtplib
from email.mime.text import MIMEText

with open('mail') as file:
    key = file.read()
    keys = key.split(',')
    username = keys[0].strip()
    password = keys[1].strip()

msg = MIMEText("The body of the email is here")
msg['Subject'] = "An Email Alert"
msg['From'] = "abc7988se@gmail.com"
msg['To'] = "abc7988jpse@gmail.com"

s = smtplib.SMTP('smtp.gmail.com:587')
s.elho()
s.starttls()
s.login(username, password)
s.send_message(msg)
s.quit()