import json
from urllib.request import urlopen, Request

def getCountry(ipAddress):
    request = Request("http://freegeoip.net/json/"+ipAddress,\
        headers={\
        'Upgrade-Insecure-Requests':'1',\
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',\
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',\
        })

    response = urlopen(request).read().decode('utf-8')
    responseJson = json.loads(response)

    return responseJson.get('country_code')

print(getCountry('50.78.253.58'))
