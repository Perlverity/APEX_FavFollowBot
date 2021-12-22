import json
from time import sleep

# import settings
import tweepy
import os

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)
word = {1:'Apex自己紹介カード', 2:'絵師', 3:'イラスト'}
# 絵師 pixiv イラスト
set_count = 20
set_result_type = ('recent.')
results = api.search(q=word[1], count=set_count, result_type=set_result_type)

for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    # print('ユーザーID:' + str(user_id))
    user = result.user.name
    # print('ユーザー名:' + user)
    tweet = result.text
    print('ユーザーのコメント:' + tweet)
    if hasattr(result, 'extended_entities'):
        try:
            if '代行' in tweet:
                print('代行は除外します')
            else:
                api.create_favorite(user_id)
                api.create_friendship(username)
                print(user + 'をフォローと「いいね」をしました\n\n')
        except:
            print(user + 'は既にフォローしています\n\n')

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()