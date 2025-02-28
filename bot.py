import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the NewsAPI key from the environment variables
newsapi_key = os.getenv("NEWSAPI_KEY")

# Define the endpoint for the NewsAPI
url = 'https://newsapi.org/v2/everything'

# Define query parameters for fetching crypto-related news
params = {
    'q': 'cryptocurrency OR bitcoin OR ethereum',  # Keywords to search for
    'pageSize': 5,  # Number of results per request
    'apiKey': newsapi_key  # Your NewsAPI key
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    news_data = response.json()
    articles = news_data['articles']
    
    # Print the titles of the articles
    for article in articles:
        print(article['title'])
        print(article['description'])
        print(f"Read more: {article['url']}")
        print("------")
else:
    print("Failed to retrieve news")
