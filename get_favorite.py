import json, config
import tweepy
from time import sleep

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

i = 0
for i in range(5):
    api.create_favorite(id=api.home_timeline()[0].id)
    print('いいねしました！')
    sleep(30)