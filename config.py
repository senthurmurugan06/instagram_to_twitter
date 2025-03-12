import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY="sk-None-OpnaOEhD1GYfJiwmiSYIT3BlbkFJ7k3NOLvIhAKQYgrT191J"
TWITTER_API_KEY = "lgim9kKYjmZ4TBeIAa7dd5vLj"

TWITTER_API_SECRET ='zXrAxcLoO65BKoFewB77LqzL0OKhTbKfQvT5JKlSt5l81cR9w1'
TWITTER_ACCESS_TOKEN ='1899662683613614080-lCPWLrKb1h274Wes9ydpSXpsgmRMSB'
TWITTER_ACCESS_SECRET ='aZ4qzoi5JTU4epcRhJFmGMp9mQbGZpu2c4zLV7BuqTAjo'

# Debugging: Print API keys to check if they're loaded
print("TWITTER_API_KEY:", TWITTER_API_KEY)
print("TWITTER_API_SECRET:", TWITTER_API_SECRET)

if not TWITTER_API_KEY or not TWITTER_API_SECRET:
    raise ValueError("Twitter API keys are missing. Check your .env file and ensure variables are loaded correctly.")
