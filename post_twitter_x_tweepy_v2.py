
"""
Post a tweet on X (Twitter) using Tweepy
----------------------------------------
Create a developer app and set env vars:
  - TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
pip install tweepy
"""
import os, tweepy

API_KEY = os.getenv("TWITTER_API_KEY", "your_api_key")
API_SECRET = os.getenv("TWITTER_API_SECRET", "your_api_secret")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "your_access_token")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "your_access_secret")

def main():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status("Hello Twitter! 🚀 This is a post from Python.")
    print("Tweet posted!")

if __name__ == "__main__":
    main()
