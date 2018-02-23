import tweepy
import json
from tweepy import OAuthHandler



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)
for status in stuff:
    t = json.dumps(status._json)
    test = json.loads(t)
    # print(type(test))
    # print(t)
    if len(test['entities']['user_mentions']) > 0:
        print(test['entities']['user_mentions'][0]["screen_name"])

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# user = api.get_user('elonmusk')
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name
# print(user)