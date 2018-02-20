from urllib.request import urlopen

with open('gappkey') as file:
    key = file.read()
    token = key.strip()

geocode = urlopen("https://maps.googleapis.com/maps/api/geocode/json?address=1+Science+Park+Boston+MA+02114&key="\
                    +token)
print(geocode.read())

timezone = urlopen("https://maps.googleapis.com/maps/api/timezone/json?location=42.3679381,-71.07111&timestamp=1412649039&key="\
                    +token)
print(timezone.read())

height = urlopen("https://maps.googleapis.com/maps/api/elevation/json?locations=42.3679381,-71.07111&key="\
                    +token)
print(height.read())