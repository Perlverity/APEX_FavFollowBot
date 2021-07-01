import json
from time import sleep

import settings
import tweepy

CK = settings.CONSUMER_KEY
CS = settings.CONSUMER_SECRET
AT = settings.ACCESS_TOKEN
ATS = settings.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

i = 0
for i in range(5):
    api.create_favorite(id=api.home_timeline()[0].id)
    print('いいねしました！')
    sleep(30)