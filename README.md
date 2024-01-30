# ShriShri001_v1.0

As the situation in India is not good for getting medical facilities and resources so Shri shares the top websites where all resources are updated from time to time by retweeting and replying them.

👇 Click on this icon to meet Shri:

<a href="https://twitter.com/ShriShri001" target="_blank" rel="noopener noreferrer"> <img src=http://assets.stickpng.com/images/580b57fcd9996e24bc43c53e.png width=35px/> 
</a>

## Prerequisites

Before using the script, make sure to install the required library:
```
pip install tweepy
```

## Setting Up Twitter API Keys

To get started, you'll need to set up your Twitter API keys. Head over to the [Twitter Developer portal](https://developer.twitter.com/en) to obtain your 
- api_key,
- api_secret_key,
- access_token, and
- access_token_secret.
  
Replace the placeholders in the script with your actual API keys.

## Running the Script
Execute the script to start fetching tweets with specific hashtags. 
Here's an example using the #ICUBeds hashtag:
```
bot('#ICUBeds')
```


## How the Bot Works
The bot function takes one or more hashtags as arguments and searches for tweets containing these hashtags. It retrieves 30 tweets (can be adjusted by changing ```rpp=20```). For each tweet, it extracts the tweet ID and text.

## Retweeting and Replying
The script attempts to retweet and reply to each fetched tweet with essential COVID-19 resource links. If a tweet has already been retweeted, the script catches the exception and continues to the next tweet, but this was not the case with early tweets where it spammed [replies](https://x.com/shahaarrif/status/1392575333870624769?s=20)

## Resource Links
The [reply](https://x.com/ShriShri001/status/1393660312436551685?s=20) includes links to prominent COVID-19 resource websites in India.

## Rest Period
To comply with Twitter API rate limits, the script pauses for 3 seconds after processing each set of tweets.

## Example Hashtags
The script is demonstrated using the #ICUBeds hashtag, but you can use other relevant hashtags for different resource categories that are trending on Twitter like '#COVIDEmergency', '#COVIDEmergencyIndia', '#Covid19IndiaHelp', '#oxygenneeded', '#कोविड१९भारतसेवा', '#oxygenneeded','#UrgentHelp'.

## Output
After execution, the script prints the total number of unique and duplicate tweet IDs and texts.


