import json
from time import sleep
import time

import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')

import tweepy
import os
import re

# CONSUMER_KEY = os.environ['CONSUMER_KEY']
# CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
# ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

CONSUMER_KEY        = 'qTKa3BJRjlBczgWyDXmI32Wwz'
CONSUMER_SECRET = '9hF65SGaUz74NLMKp4oNuODS0SLxbgiWwk6kSMEY9yCHZsuvlN'
ACCESS_TOKEN        = '1343743642213609473-YoC8HZpttn7HNqwPFIyKISYhHv4qy8'
ACCESS_TOKEN_SECRET = 'rLIdznOdvNq0Qej7NDEMNskENBVPuOn2tatdoB4Lt1kBE'

# CK = CONSUMER_KEY
# CS = CONSUMER_SECRET
# AT = ACCESS_TOKEN
# ATS = ACCESS_TOKEN_SECRET

import settings
CK = settings.CONSUMER_KEY
CS = settings.CONSUMER_SECRET
AT = settings.ACCESS_TOKEN
ATS = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth, wait_on_rate_limit=True)
my_user_id = api.verify_credentials().id_str

# フォロー返し
cnt = 0

# フォロワー数とフォロー数を格納するリストを用意
follower_list = []
friend_list = []

# ユーザ情報からフォロワー数を取得、格納
follower_list = api.get_follower_ids()

# ユーザ情報からフォロー数を取得、格納
friend_list = api.get_friend_ids()

result_list = list(set(friend_list) - set(follower_list))

api_limit = 0
# 相互じゃないユーザーのフォローを解除する
for following in follower_list:
    if following not in follower_list and api_limit < 25:
        time.sleep(random.randrange(1,10,1))
        user  = api.get_user( id = following)
        userfollowers  = user.followers_count
        api_limit += 1
        unfollow_user += 1

# for user_id in result_list:
#     cnt = cnt + 1
#     try:
#         if cnt < 1000:
#             api.destroy_friendship(user_id=user_id)
#     except Exception as e:
#         print(e)
