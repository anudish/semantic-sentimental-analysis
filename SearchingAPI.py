import os
import tweepy as tw
import csv
import re
import _json
import json

ACCESS_TOKEN = "1232331328072437765-Z92UuD77zybNNQzkzxmRRZ5DsFVJ7t"
ACCESS_TOKEN_SECRET = "hVSs31w04d8XOSbwUzvwctz9GdURDt3vBHnKnONBuAsyi"
CONSUMER_KEY = "O7O3nuMljdkxzYxU3lT5I29P0"
CONSUMER_KEY_SECRET = "u24EU8mlWiZVL75YTMIV57laQ0hH2Q5qZI5VMxQgPJX64nCkY1"
tweetArray=[]
auth = tw.OAuthHandler(CONSUMER_KEY ,CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)
date_since = "2020-01-01"
tweets = tw.Cursor(api.search,
                   q='Canada OR University OR Dalhousie University OR Halifax OR Canada Education OR Moncton OR Toronto',
                   lang="en",
                   since=date_since).items(3010)

with open('twitterData.txt', 'w+') as file:
    for i in tweets:
        j = i.text
        j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', j)
        j = j.strip()
        i.text = j
        data = 'Tweet: ' + j + '\n'
        file.write(data)