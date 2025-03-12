from flask import Flask, request, jsonify
from instagram_scraper import fetch_instagram_post
from summarizer import summarize_text
from twitter_api import post_tweet

app = Flask(__name__)


@app.route('/post-latest', methods=['GET'])
def post_latest():
    try:
        # Fetch Instagram post
        caption, image_url = fetch_instagram_post("sivaram_ofl")

        if not caption:
            return jsonify({"error": "Failed to fetch Instagram post"}), 500

        # Summarize caption
        tweet_text = summarize_text(caption)

        # Post to X.com (Twitter)
        response = post_tweet(tweet_text)

        return jsonify({"tweet": tweet_text, "image_url": image_url, "twitter_response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
