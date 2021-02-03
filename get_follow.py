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
word = {1:'pixiv', 2:'絵師', 3:'イラスト'}
# 絵師 pixiv イラスト 
set_count = 20
set_result_type = ('recent.')
results = api.search(q=word[3], count=set_count, result_type=set_result_type)

for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    print('ユーザーID:' + str(user_id))
    user = result.user.name
    print('ユーザー名:' + user)
    tweet = result.text
    print('ユーザーのコメント:' + tweet)
    try:
        api.create_favorite(user_id)
        api.create_friendship(username)
        print(user + 'をフォローと「いいね」をしました\n\n')
    except:
        print(user + 'は既にフォローしています\n\n')