import config
import tweepy

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)
word = {1:'pixiv', 2:'絵師', 3:'イラスト'}
# 絵師 pixiv イラスト
set_count = 20
set_result_type = ('recent.')
results = api.search(q=word[3], count=set_count, result_type=set_result_type)
for result in results:
    username = result.user.name
    user_id = result.user.id
    tweet = result.text
    tweet_id = result.id
    print('ユーザー名:' + username)
    print('ユーザーID:' + str(user_id))
    print('---------------------------------------')
    try:
        api.retweet(tweet_id) #RTする
        print(tweet)
        print('---------------------------------------')
        print('をRTしました\n\n')
        print('---------------------------------------')
    except:
        print(tweet)
        print('---------------------------------------')
        print('をRTしてます\n\n')
        print('---------------------------------------')

