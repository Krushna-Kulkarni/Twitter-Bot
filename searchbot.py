import tweepy
import time
                             #key                          #secretKey
auth = tweepy.OAuthHandler('x3l3P99FCuBtVQOYGRGsfQBNS', 'oRDstqWhUZlPTY0ufDN2WprQsz8E8RFLx4URjtMK1B8LByYr8w')
auth.set_access_token('1309414393591943168-HhFkjct8hOKermF5wiPkg0m82384Sk', 'MNFpLNhU4IIK91XvuChYdC9NiYWNFr8DZIb4m3tyoe6cz')

api = tweepy.API(auth)


hashtag = "#twitterbot"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

for tweet in tweets:
    try:
        tweet.retweet()
        print("Retweet Done")
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(2)