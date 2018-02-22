from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator
import itertools
def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but","we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their","can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will","as", "up", "one", "time", "has", "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False

def clean_text(input):
    input = re.sub('\n+', " ", input).lower()
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, 'UTF-8')
    input = input.decode("ascii", "ignore")
    return input

def clean_input(input):
    input = clean_text(input)
    clean_input = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i') :
            clean_input.append(item)
    return clean_input

def ngrams(input, n):
    input = clean_input(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
        
    return output

def getFirstSentenceContaining(ngram, content):
    sentences = content.split(".")
    for sentence in sentences:
        if ngram in sentence:
            return sentence
    return ""

content = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read()
    , 'utf-8')
ngrams = ngrams(content, 2)
ngrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)

print("2-grams count is: " + str(len(ngrams)))

for i in range(0,10):
    for item in ngrams:
        if isCommon(item[0].split(' ')):
            ngrams.remove(item)
            
print(ngrams[:50])

for ngram in ngrams[:5]:
    print(getFirstSentenceContaining(ngram[0], content.lower()))
