from twitter import *

with open('apikey') as file:
    key = file.read()
    keys = key.split(',')
    access_token = keys[0].strip()
    access_token_secret = keys[1].strip()
    consumer_key = keys[2].strip()
    consumer_secret = keys[3].strip()

t = Twitter(auth=OAuth(access_token, access_token_secret,\
            consumer_key, consumer_secret))

'''트윗을 가져온다.
pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)
'''

'''상태를 업데이트한다.
statusUpdate = t.statuses.update(status='Hello,World!')
print(statusUpdate)
'''


'''목록을 가져온다
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)
'''
