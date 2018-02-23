import tweepy
import json
import key_token
import queue

queue = queue.Queue()

auth = tweepy.OAuthHandler(key_token.consumer_key, key_token.consumer_secret)
auth.set_access_token(key_token.access_token, key_token.access_token_secret)

api = tweepy.API(auth)

tweetsReplies = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)
for tweetReply in tweetsReplies:
    twRe = json.dumps(tweetReply._json)
    tR = json.loads(twRe)
    if len(tR['entities']['user_mentions']) > 0:
        replyUser = tR['entities']['user_mentions'][0]["screen_name"]
        ReplyQueue = queue.insert(replyUser)
