import tweepy
import requests

# Twitter API credentials
API_KEY = "your_twitter_api_key"
API_SECRET = "your_twitter_api_secret"
ACCESS_TOKEN = "your_twitter_access_token"
ACCESS_SECRET = "your_twitter_access_secret"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# NewsAPI credentials
NEWS_API_KEY = "your_newsapi_key"
url = f"https://newsapi.org/v2/everything?q=crypto&domains=coindesk.com&apiKey={NEWS_API_KEY}"

# Fetch the news from CoinDesk
response = requests.get(url).json()

# Get the latest 1 news article and format it for Twitter
article = response["articles"][0]
title = article["title"]
link = article["url"]

# Prepare the tweet
tweet = f"🚨 {title}\n🔗 {link} #Bitcoin #Crypto #CoinDesk"

# Post the tweet
api.update_status(tweet)

print("Tweet posted successfully!")
