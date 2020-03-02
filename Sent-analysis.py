import tweepy
import csv
import json
from textblob import TextBlob
import sys

# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
    info = json.load(cred_data)
    consumer_key = info['CONSUMER_KEY']
    consumer_secret = info['CONSUMER_SECRET']
    access_key = info['ACCESS_KEY']
    access_secret = info['ACCESS_SECRET']
    
# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.

num_tweets = \
int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')
sent = "null"
for tweet in tweepy.Cursor(api.search, q='#' + hashtag,
count=100).items(num_tweets):
    with open('tweets_' + hashtag + '.csv', 'a') as \
    f:
        tweetline = str(tweet.text.encode('utf-8'))
        analysis = TextBlob(tweetline)     

        if analysis.sentiment[0]>0:
            sent = "Positive"
            f.write("%s\n" % str(sent))
        elif analysis.sentiment[0]<0:
            sent = "Negative"
            f.write("%s\n" % str(sent))
        else:
            sent = "Neutral"
            f.write("%s\n" % str(sent))

print ('Extracted ' + str(num_tweets) \
+ ' tweets with hashtag #' + hashtag)
