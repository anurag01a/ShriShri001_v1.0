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
  
  global count
  count=0
  
  print(datetime.datetime.now())
 
    
  for tweet in twitter.Cursor(api.search, q=hashtag, lang="en", rpp=20).items(30):
 
      try:
       
          id = dict(tweet._json)['id']
          ids.append(id)
          text=dict(tweet._json)['text']
          tweets.append(text)
 
          
          if text in set(tweets):
 
              api.update_status(status = 'Kindly Check https://covidwin.in/, https://life.coronasafe.network/, https://indiacovidresources.in/, https://covidfightclub.org/, https://covidrelief.glideapp.io/, https://external.sprinklr.com/insights/explorer/dashboard/, https://covid19-twitter.in/, https://covidtools.in/, https://covid.army/'+str(count),
                              in_reply_to_status_id = id, auto_populate_reply_metadata=True)
           
              api.retweet(id)
             #api.create_favourite(id)
 
              print("Tweet ID:",id)
          
              print("Tweet Text:",text)
          
            #ids.append(id)
               
          else:
 
              print("Already retweeted and replied to this tweet !! Bot re-executing\n")
              bot('#ICUBeds')
 
            
      except twitter.TweepError as e:
        
        print(e.reason)
        print("Tweet Text:",text)
 
  count=count+1
  print("Let the tweepy rest !! \n")
  time.sleep(3)
  bot('#ICUBeds')
 
#bot('#कोविड१९भारतसेवा')
#bot('#oxygenneeded')
bot('#ICUBeds')
#bot('#COVIDEmergency')
#bot('#COVIDEmergencyIndia')
#bot('#Covid19IndiaHelp')
