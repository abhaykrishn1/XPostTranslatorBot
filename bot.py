import tweepy
import tweepy.client
import config as c



client = tweepy.Client(c.bearer_token,c.api_key,c.api_secret,c.access_token,c.access_token_secret)

auth = tweepy.OAuth1UserHandler(c.api_key,c.api_secret,c.access_token,c.access_token_secret)

api = tweepy.API(auth)

client.create_tweet(text="Hii we are translators...!!")


