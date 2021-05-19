#pip install tweepy

import tweepy as twitter

import datetime
import time

auth = twitter.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api=twitter.API(auth,wait_on_rate_limit=True)
 
ids=[]
tweets=[]
def bot(*hashtag):
  
  global unique_count
  unique_count=0

  global duplicate_count
  duplicate_count=0
  
  print(datetime.datetime.now())
 
  for tweet in twitter.Cursor(api.search, q=hashtag, lang="en", rpp=20).items(30):
       
      id = dict(tweet._json)['id']
      ids.append(id)
      text=dict(tweet._json)['text']
      tweets.append(text)

          #print(tweet)

      while True:

          try:
 
              api.update_status(status = 'Kindly Check https://covidwin.in/, https://life.coronasafe.network/, https://indiacovidresources.in/, https://covidfightclub.org/, https://covidrelief.glideapp.io/, https://external.sprinklr.com/insights/explorer/dashboard/, https://covid19-twitter.in/, https://covidtools.in/, https://covid.army/'+str(count),
                              in_reply_to_status_id = id, auto_populate_reply_metadata=True)
           
              api.retweet(id)
              #api.create_favourite(id)
              print("Tweet ID:",id)
              print("Tweet Text:",text)
              unique_count = unique_count+1
              #ids.append(id)
               
          except twitter.TweepError as e:
        
              print(e.reason)
              #print("Tweet Text:",text)
              print("Already retweeted and replied to this tweet !! Bot re-executing\n")
              duplicate_count = duplicate_count+1
              break
 
  print("Let the tweepy rest !! \n")
  time.sleep(3)
  #bot('#oxygenneeded')
 
#bot('#कोविड१९भारतसेवा')
#bot('#oxygenneeded')
#bot('#UrgentHelp')
bot('#ICUBeds')
#bot('#COVIDEmergency')
#bot('#COVIDEmergencyIndia')
#bot('#Covid19IndiaHelp')
   
print("Total ids :",len(ids),"\nTotal Set ids :",len(set(ids)))
print("Total Tweets :",len(tweets),"\nTotal Set Tweets :",len(set(tweets)))
print("Unique iterations: ",unique_count,"\nDuplicate iterations: ",duplicate_count)
