import tweepy
import os
from config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)

def post_tweet(tweet_text):
    try:
        tweet = api.update_status(tweet_text)
        return {"tweet_id": tweet.id, "tweet_url": f"https://x.com/user/status/{tweet.id}"}
    except Exception as e:
        return {"error": str(e)}
