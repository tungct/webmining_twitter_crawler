import tweepy
import json
import key_token

auth = tweepy.OAuthHandler(key_token.consumer_key, key_token.consumer_secret)
auth.set_access_token(key_token.access_token, key_token.access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)
for status in stuff:
    t = json.dumps(status._json)
    test = json.loads(t)
    if len(test['entities']['user_mentions']) > 0:
        print(test['entities']['user_mentions'][0]["screen_name"])
