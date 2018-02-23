import tweepy
import json
from tweepy import OAuthHandler

consumer_key = "luQ9n0TBdf1V8egNNcKwuk94l"
consumer_secret = "hpENWe1p8YrgaajPDzOe0PPODIq4hWZVn9rH0mVZ8onaC0LxYz"
access_token = "966901044822212608-ZMiHf1ZHleGZjhyZXoOzydKVoAAGAit"
access_token_secret = "CsMJtixeYY1DkUMo12KsCsC49TxTF7wDaxFjHrGIMv4RJ"

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