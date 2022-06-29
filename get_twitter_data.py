'''

    DISCOVERED I NEED A PREMIUM API KEY TO SEARCH FULL TWITTER ARCHIVE.
    Life is Dukkha.
    :Sad Face: :Sad Face: :Sad Face: :Sad Face: :Sad Face: :Sad Face:

'''



import requests
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_token = os.getenv('TWTTR_API_KEY')

consumer_secret = os.getenv('TWTTR_API_SCRT_KEY')

access_token = os.getenv('TWTTR_ACCESS_TKN')

access_token_secret = os.getenv('TWTTR_ACCESS_TKN_SCRT')

bearer = os.getenv('TWTTR_BEARER_TKN')




auth = tweepy.OAuth1UserHandler(
  consumer_token, 
  consumer_secret, 
  access_token,
  access_token_secret
)

api = tweepy.API(auth)

client = tweepy.Client(
  consumer_key = consumer_token,
  consumer_secret = consumer_secret,
  access_token = access_token,
  access_token_secret = access_token_secret
)

print(client)

