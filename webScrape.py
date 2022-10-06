import config
import tweepy
from tweepy import OAuthHandler
from config import consumer_key,consumer_secret,access_secret,access_token
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)