
"""
Post an image to Instagram via Graph API (Business/Creator account)
-------------------------------------------------------------------
Steps:
  - Connect Instagram business account to a Facebook page
  - Get instagram_business_account id and long-lived access token
  Env vars: IG_ACCESS_TOKEN, IG_BUSINESS_ID, IMAGE_URL (public), CAPTION
pip install requests
"""
import os, requests, time

ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN", "your_instagram_access_token")
BUSINESS_ID = os.getenv("IG_BUSINESS_ID", "your_business_account_id")
IMAGE_URL = os.getenv("IMAGE_URL", "https://www.python.org/static/community_logos/python-logo.png")
CAPTION = os.getenv("CAPTION", "Hello Instagram! 🚀 Posted using Python.")

def main():
    create_url = f"https://graph.facebook.com/v19.0/{BUSINESS_ID}/media"
    creation = requests.post(create_url, params={
        "image_url": IMAGE_URL,
        "caption": CAPTION,
        "access_token": ACCESS_TOKEN
    }).json()
    creation_id = creation.get("id")
    print("Creation response:", creation)

    if creation_id:
        publish_url = f"https://graph.facebook.com/v19.0/{BUSINESS_ID}/media_publish"
        publish = requests.post(publish_url, params={
            "creation_id": creation_id,
            "access_token": ACCESS_TOKEN
        }).json()
        print("Publish response:", publish)

if __name__ == "__main__":
    main()
