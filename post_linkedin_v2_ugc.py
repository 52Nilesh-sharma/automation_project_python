
"""
Post a text update to LinkedIn using the REST API (UGC Post)
------------------------------------------------------------
Steps:
  1) Create LinkedIn app, get OAuth access token with w_organization_social / w_member_social
  2) Replace author URN (urn:li:person:XXXX) or set env var LINKEDIN_AUTHOR_URN
  3) Export LINKEDIN_ACCESS_TOKEN
pip install requests
"""
import os, requests, json

ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "your_access_token")
AUTHOR_URN = os.getenv("LINKEDIN_AUTHOR_URN", "urn:li:person:your_profile_id")

API_URL = "https://api.linkedin.com/v2/ugcPosts"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

payload = {
    "author": AUTHOR_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {"text": "Hello LinkedIn! Posting via Python 🚀"},
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
}

def main():
    r = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    print("Status:", r.status_code)
    print("Response:", r.text)

if __name__ == "__main__":
    main()
