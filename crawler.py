import tweepy 
import csv
import pandas as pd
##INPUT YOUR CREDENTIALS HERE.

consumer_key = 'IhmYtYbSp7yrADITwhJaY2lhQ'
consumer_secret = 'mmkrdMXv0ADfw2Zj4qIA7RkDcreX14IYgbDt26LhdVDylRy1jr'
access_token = '778635668339634176-DTq7Twl56ymsnyhrbAEX1Zk6NWPoicB'
access_token_secret = '03iN7IAxODFcmrCCey01YRsJ6BRHfI3LIvLWJBVe38swh'

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api=tweepy.API(auth , wait_on_rate_limit = True)
#### crawl ###unitedAirlines
# OPEN / CREATE FILE TO APPEND DATA.
 
csvFile = open('airlines.csv' , 'a')
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES", count=100,lang="en",since="2017-04-03").items():
	print(tweet.created_at,tweet.text)
	csvWriter.writeow([tweet.created_at,tweet.text.encode('utf-8')])