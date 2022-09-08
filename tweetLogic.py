import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
# bearer_token = os.environ.get('BEARER_TOKEN')
# v2Token = os.environ.get('V2_TOKEN')
# v2Token_secret = os.environ.get('V2_TOKEN_SECRET')
# consumer_key = os.environ.get('CONSUMER_KEY')
# consumer_secret = os.environ.get('CONSUMER_SECRET')
# client_id = os.environ.get('CLIENT_ID')
# client_secret = os.environ.get('CLIENT_SECRET')

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
v1handler = tweepy.API(auth)
# v2handler = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, 
#                         consumer_secret=consumer_secret, access_token=v2Token, 
#                         access_token_secret=v2Token_secret, wait_on_rate_limit=True)
                        
# def sendTweet(input):
#     v2handler.create_tweet(text=input)    

def sendDM(input, user_id):
    v1handler.send_direct_message(recipient_id=user_id, text=input)