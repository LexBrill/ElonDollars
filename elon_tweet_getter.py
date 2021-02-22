import os
import tweepy as tw
import pandas as pd 
import csv
import re
import string

f = open("keys.txt", "r")
consumer_key = f.readline().rstrip()
consumer_secret = f.readline().rstrip()
access_token = f.readline().rstrip()
access_token_secret = f.readline().rstrip()

auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token = (access_token,access_token_secret)
api = tw.API(auth)

tweets = tw.Cursor(api.user_timeline, user_id = "44196397", since_id = "2020-2-20", inlcude_rts = False).items(20)
for tweet in tweets: 
    print(tweet.text)



