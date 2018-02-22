from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")\
    .read().decode('ascii', 'ignore')
dataFile = StringIO(data)
#csvReader = csv.reader(dataFile)
dictReader = csv.DictReader(dataFile) # csvReader는 첫 번째 행(표의 헤더)를 무시하지 않는다.

print(dictReader.fieldnames)

'''
for row in csvReader:
    print('The album \''+row[0]+'\' was released in ' + str(row[1]))
'''

for row in dictReader:
    print(row)