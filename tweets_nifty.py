# Python Script to Extract tweets of a
# particular Hashtag using Tweepy and Pandas
 
# import modules
import pandas as pd
import tweepy
import json
import csv
import datetime
import time 

today = datetime.datetime.now()
today = today.replace(hour=23, minute=59, second=59, microsecond=999999) 
#till = today - datetime.timedelta(4) 

api = None      

# function to display data of each tweet
def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Date:{ith_tweet[0]}")
        print(f"Location:{ith_tweet[1]}")
        print(f"Follower Count:{ith_tweet[2]}")
        print(f"Retweet Count:{ith_tweet[3]}")
        print(f"Tweet Text:{ith_tweet[4]}")
 
 
# function to perform data extraction
def scrape(days,filename):
        till = today - datetime.timedelta(days) 
        # Creating DataFrame using pandas
        db = pd.DataFrame(columns=['Date','Location','Followers','Retweets','Text'])
 
        # We are using .Cursor() to search
        # through twitter for the required tweets.
        # The number of tweets can be
        # restricted using .items(number of tweets)
        print(till.date())
        qry =  "nifty50"
        tweets = tweepy.Cursor(api.search_tweets,
                               q=qry, lang="en", until = till.date(),
                               tweet_mode='extended').items(1000)
        # tweets = tweepy.Cursor(api.search_tweets,  
        #                         q="#nifty50",
        #                         since_id="2022-01-08", 
        #                         count=numtweet).items()
 
 
        # .Cursor() returns an iterable object. Each item in
        # the iterator has various attributes
        # that you can access to
        # get information about each tweet
        list_tweets = [tweet for tweet in tweets]
 
        # Counter to maintain Tweet Count
        i = 1
 
        # we will iterate over each tweet in the
        # list for extracting information about each tweet
        for tweet in list_tweets:
                #username = tweet.user.screen_name
                #description = tweet.user.description
                date = tweet.created_at
                location = tweet.user.location
                #following = tweet.user.friends_count
                followers = tweet.user.followers_count
                #totaltweets = tweet.user.statuses_count
                retweetcount = tweet.retweet_count
                #hashtags = tweet.entities['hashtags']
 
                # Retweets can be distinguished by
                # a retweeted_status attribute,
                # in case it is an invalid reference,
                # except block will be executed
                try:
                        text = tweet.retweeted_status.full_text
                except AttributeError:
                        text = tweet.full_text
                # hashtext = list()
                # for j in range(0, len(hashtags)):
                #         hashtext.append(hashtags[j]['text'])
 
                # Here we are appending all the
                # extracted information in the DataFrame
                ith_tweet = [date,location,followers,retweetcount,text]
                db.loc[len(db)] = ith_tweet
 
                # Function call to print tweet data on screen
                #printtweetdata(i, ith_tweet)
                i = i+1
        #filename = 'Date6.csv'
 
        # we will save our database as a CSV file.
        db.to_csv(filename)

def init() : 
        global api
        with open('keys.json') as f: twitter_keys = json.load(f)
        auth = tweepy.OAuthHandler(twitter_keys["consumer_key"], twitter_keys["consumer_secret"])
        auth.set_access_token(twitter_keys["api_key"], twitter_keys["api_secret"])
        api = tweepy.API(auth)
 
if __name__ == '__main__':
       
        init()

        #words = input()
        #date_since = input()

        #numtweet = 1000
        scrape(2,'Nifty 50 Data\\Jan-10.csv')
        # for i in range(9,10) : 
        #         name = "Nifty 50 Data\\"
        #         if(i<=8) : name = name + f"Jan-0{9-i}"
        #         else :
        #                 name = name + "Dec-"
        #                 date = 40-i
        #                 if(date<10) : name = name + "0"
        #                 name = name + str(date)
        #         name = name + ".csv"
        #         print(name)
                
        #         scrape(i,name)
                # except :
                #     time.sleep(500)
                #     try : scrape(i,name)
                #     except :
                #         print("Excecution stopped at",i)
                #         break 
                #time.sleep(300)