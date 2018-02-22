import requests

params = {'firstname':'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)


import request
files = {'uploadFile':open('..', 'rb')}
r = request.post("http://pythonscraping.com/pages/prop.php" files=files)
print(r.text)