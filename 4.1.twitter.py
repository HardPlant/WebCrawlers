from twitter import *


with open('apikey') as file:
    key = file.read()
    keys = key.split(',')
    access_token = keys[0].strip()
    access_token_secret = keys[1].strip()
    consumer_key = keys[2].strip()
    consumer_secret = keys[3].strip()
print(access_token)
print(access_token_secret)
print(consumer_key)
print(consumer_secret)

t = Twitter(auth=OAuth(access_token, access_token_secret,\
            consumer_key, consumer_secret))

pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)
