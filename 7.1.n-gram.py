from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter
from collections import OrderedDict

import itertools

def clean_input(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, 'UTF-8')
    input = input.decode("ascii", "ignore")
    input = input.upper()
    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            clean_input.append(item)

    return clean_input

def ngrams(input, n):
    input = clean_input(input)
    #print(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(" ".join((input[i:i+n])))
        
    return Counter(output)
    

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t:t[1], reverse=True))
x = itertools.islice(ngrams.items(), 0, 5)
for key, value in x:
    print("{} : {}".format(key,value))
print("2-grams count is: " + str(len(ngrams)))