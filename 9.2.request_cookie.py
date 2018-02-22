import requests
session = requests.Session()

params = {'username':'Ryan', 'password':'password'}
r=session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to:")
print(r.cookies.get_dict())
r = session.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)
