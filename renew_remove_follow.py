import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import tweepy

keys = dict(
screen_name = '@Elmas_Crypt3',
consumer_key = 'qTKa3BJRjlBczgWyDXmI32Wwz',
consumer_secret = '9hF65SGaUz74NLMKp4oNuODS0SLxbgiWwk6kSMEY9yCHZsuvlN',
access_token = '1343743642213609473-YoC8HZpttn7HNqwPFIyKISYhHv4qy8',
access_token_secret = 'rLIdznOdvNq0Qej7NDEMNskENBVPuOn2tatdoB4Lt1kBE',
)

SCREEN_NAME = keys['screen_name']
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

followers = api.get_follower_ids(screen_name=SCREEN_NAME)
friends = api.get_friend_ids(screen_name=SCREEN_NAME)

cnt = 0
for f in friends[::-1]:
    if cnt >= 300:
        break
    if f not in followers:
        cnt += 1
        print("ID:{}のフォローを解除しました。".format(api.get_user(user_id=f).screen_name))
        api.destroy_friendship(user_id=f)