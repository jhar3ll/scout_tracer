import tweepy
access_token = '1470520489609211911-B5fjeZxgJBF5zcml4VY9TKpDtUBOJq'
access_token_secret = 'V0xuzEZY4e58KtmjeCD9HA3S9rs0ampHa814LIVLYVUss'
api_key = '3M1t2JclfQitgRexVohwwHWfQ'
api_key_secret = 'JtOCKyQ00s4xvfY76JNXK4DIm5MdUGcWBIFayWM3k4ocbZzOep'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADcBfgEAAAAAb7x7Fs6Cg1RIqoiPfGMMg1qYWWk%3DGESW42Y1hIGSX3FjpqFs9C70ZeTLdU5fIapd61u98kXu0v0BCq'
token = "135039188-ahQHS7tRw8vxsJsFTiIFfpvMzA5zvZckd20Tj98l"
token_secret = "VxYJmPdD7XPxiUA89UkADvRStshxJNNpaVtyMKcu7nOyp"
consumer_key = "LqOENp4h3s9Xr1dSgpFdPz9Z3"
consumer_secret = "W7yvDsHOkcbTvpp0FqnIHCSVS94FTJjEXbYGawasE4g1lNsj4n"
client_id = "aG5sUUV6TVJwMnpGN2d0QTJZTjU6MTpjaQ"
client_secret = "2qg0xQ3Gw29VM6Y0BYfIF75Xhz6rQePkorFBK8zkDHWfJY3etN"

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
v1handler = tweepy.API(auth)
v2handler = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, access_token=token, 
                        access_token_secret=token_secret, wait_on_rate_limit=True)
                        
def sendTweet(input):
    v2handler.create_tweet(text=input)    

def sendDM(input, user_id):
    v1handler.send_direct_message(recipient_id=user_id, text=input)