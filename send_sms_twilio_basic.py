
"""
Send an SMS using Twilio
------------------------
1) Sign up at https://twilio.com, get ACCOUNT_SID, AUTH_TOKEN
2) Buy/verify a phone number
3) Export environment variables:
   - TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM, TWILIO_TO
pip install twilio
"""
import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_account_sid")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
FROM_NUMBER = os.getenv("TWILIO_FROM", "+1234567890")
TO_NUMBER = os.getenv("TWILIO_TO", "+919876543210")

def main():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Hello, this is a test SMS from Python!",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
    print("SMS sent successfully! Message SID:", message.sid)

if __name__ == "__main__":
    main()
