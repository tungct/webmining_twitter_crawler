import tweepy
import json
import key_token
class Queue:
    def __init__(self):
        self.items = []

    def insert(self, x):
        self.items.append(x)
        return self.items
    def pop(self):
        first =  self.items[0]
        del self.items[0]
        return first

auth = tweepy.OAuthHandler(key_token.consumer_key, key_token.consumer_secret)
auth.set_access_token(key_token.access_token, key_token.access_token_secret)

api = tweepy.API(auth)

stuff = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)
for status in stuff:
    t = json.dumps(status._json)
    test = json.loads(t)
    # print(type(test))
    # print(t)
    if len(test['entities']['user_mentions']) > 0:
        print(test['entities']['user_mentions'][0]["screen_name"])

queue = Queue()
print queue #should show something like <__main__.Queue instance at 0x(some numbers here)>
newQueue = queue.insert(5)
newQueue = queue.insert("test")
print newQueue
print(queue.pop())
print newQueue[0]
print(len(newQueue))

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# user = api.get_user('elonmusk')
# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#    print friend.screen_name
# print(user)