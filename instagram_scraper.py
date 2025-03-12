import requests
from bs4 import BeautifulSoup
import json
import instaloader


def fetch_instagram_post(username):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)

    for post in profile.get_posts():
        caption = post.caption
        image_url = post.url
        return caption, image_url

    return None, None

#
# def fetch_instagram_post(username):
#     url = f"https://www.instagram.com/{username}/"
#
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }
#
#     response = requests.get(url, headers=headers)
#
#     print("Response Status Code:", response.status_code)  # Debugging
#
#     if response.status_code != 200:
#         print("Error: Unable to fetch Instagram page")
#         return None, None
#
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     print("Page Content:", soup.prettify()[:1000])  # Print first 1000 characters
#
#     script_tag = soup.find("script", text=lambda t: t and "window.__additionalDataLoaded" in t)
#
#     if not script_tag:
#         print("Error: Instagram page structure might have changed.")
#         return None, None
#
#     try:
#         json_text = script_tag.string.split("window.__additionalDataLoaded(")[1].strip(");")
#         json_data =json.loads(json_text)
#
#         post = json_data["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]
#         caption = post["edge_media_to_caption"]["edges"][0]["node"]["text"]
#         image_url = post["display_url"]
#
#         return caption, image_url
#
#     except Exception as e:
#         print("Error parsing JSON:", str(e))
#         return None, None
