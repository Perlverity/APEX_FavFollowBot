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
my_user_id = api.me().id_str

# フォロー返し
cnt = 0

# フォロワー数とフォロー数を格納するリストを用意
follower_list = []
friend_list = []

# ユーザ情報からフォロワー数を取得、格納
follower_list = api.followers_ids(my_user_id)

# ユーザ情報からフォロー数を取得、格納
friend_list = api.friends_ids(my_user_id)

result_list = list(set(follower_list) - set(friend_list))

for user_id in result_list:

    cnt = cnt + 1
    print(user_id)

    try:
        if cnt < 3:
            api.create_friendship(user_id)
            print('---------------------------------------')
            print('フォローしました。\n\n')
            print('---------------------------------------')
    except Exception as e:
        print(e)
