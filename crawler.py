import tweepy
import json
import key_token
import queue

queue = queue.Queue()
userList = []
userPair = []

auth = tweepy.OAuthHandler(key_token.consumer_key, key_token.consumer_secret)
auth.set_access_token(key_token.access_token, key_token.access_token_secret)

api = tweepy.API(auth)
userList.append('elonmusk')

tweetsReplies = api.user_timeline(screen_name = 'elonmusk', count = 100, include_rts = True)
for tweetReply in tweetsReplies:
    twRe = json.dumps(tweetReply._json)
    tR = json.loads(twRe)
    if len(tR['entities']['user_mentions']) > 0:
        replyUser = tR['entities']['user_mentions'][0]["screen_name"]
        ReplyQueue = queue.insert(replyUser)

count = 0
check = 0
while(len(ReplyQueue) != 0):
    # print(ReplyQueue[0])
    user = queue.pop()
    if user not in userList:
        userList.append(user)
        with open("userList.txt", "a") as userFile:
            userFile.write(replyUser + "\n")
            userFile.close()
    try:
        tweetsReplies = api.user_timeline(screen_name=user, count=20, include_rts=True)
        for tweetReply in tweetsReplies:
            twRe = json.dumps(tweetReply._json)
            tR = json.loads(twRe)
            if len(tR['entities']['user_mentions']) > 0:
                replyUser = tR['entities']['user_mentions'][0]["screen_name"]
                ReplyQueue = queue.insert(replyUser)
                if replyUser not in userList:
                    userList.append(replyUser)
                    with open("userList.txt", "a") as userFile:
                        userFile.write(replyUser + "\n")
                        userFile.close()
                pair = user + "-" +replyUser
                if pair not in userPair:
                    userPair.append(pair)
                    with open("userPair.txt", "a") as pairFile:
                        pairFile.write(pair + "\n")
                        pairFile.close()
                print("Lenght userPair : ", len(userPair))
                print("Lenght userList : ", len(userList))
                count = count + 1
                print(count)
                if count == 100000:
                    check = 1
                    break
    except Exception as error:
        print('Caught this error: ' + repr(error))
    if check == 1:
        break