import tweepy
import time
                             #key                          #secretKey
auth = tweepy.OAuthHandler('x3l3P99FCuBtVQOYGRGsfQBNS', 'oRDstqWhUZlPTY0ufDN2WprQsz8E8RFLx4URjtMK1B8LByYr8w')
auth.set_access_token('1309414393591943168-HhFkjct8hOKermF5wiPkg0m82384Sk', 'MNFpLNhU4IIK91XvuChYdC9NiYWNFr8DZIb4m3tyoe6cz')

api = tweepy.API(auth)

#Use "PythonEverywhere" to deploy your bot 




''' to print each tweet of the above account'''
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


''''To print followers count and names of friends'''
# user = api.get_user('PMOindia')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

''''to make a tweet'''
# api.update_status("This is a demo tweet.")
# # print("status Updated!")


FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return



def reply():
    tweets= api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied to  @" + tweet.user.screen_name + "tweet ID -" + str(tweet.id)  + "\n")
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            api.update_status("@" + tweet.user.screen_name + " Thank you for helping.", tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(15)