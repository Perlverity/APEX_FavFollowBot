import json
from time import sleep
import time

import tweepy
import os
import re

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET

# import settings
# CK = settings.CONSUMER_KEY
# CS = settings.CONSUMER_SECRET
# AT = settings.ACCESS_TOKEN
# ATS = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)
word = {1: '#メンヘラさんと繋がりたい', 2: '絵師', 3: 'イラスト'}
# 絵師 pixiv イラスト
set_count = 1
set_result_type = ('recent')
results = api.search(q=word[1], count=set_count,
                     result_type=set_result_type, lang='ja')

for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    # print('ユーザーID:' + str(user_id))
    user = result.user.name
    print('ユーザー名:' + user)
    tweet = result.text
    tweet_id = result.id
    # print('ユーザーのコメント:' + tweet)

    try:
        api.create_favorite(user_id)
        api.retweet(tweet_id)  # RTする
        api.create_friendship(username)
        print(user + 'を「いいね」をしました\n\n')

    except:
        print(user + 'はいいねできませんでした\n')

    time.sleep(3)
