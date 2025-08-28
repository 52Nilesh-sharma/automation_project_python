
"""
Post to a Facebook Page using Graph API
---------------------------------------
Requires a Page access token with pages_manage_posts.
Env vars: FB_PAGE_ACCESS_TOKEN, FB_PAGE_ID
pip install requests
"""
import os, requests

ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "your_page_access_token")
PAGE_ID = os.getenv("FB_PAGE_ID", "your_page_id")
MESSAGE = "Hello Facebook! 🚀 Posted using Python."

def main():
    url = f"https://graph.facebook.com/{PAGE_ID}/feed"
    params = {"message": MESSAGE, "access_token": ACCESS_TOKEN}
    r = requests.post(url, params=params)
    print("Status:", r.status_code)
    print("Response:", r.text)

if __name__ == "__main__":
    main()
