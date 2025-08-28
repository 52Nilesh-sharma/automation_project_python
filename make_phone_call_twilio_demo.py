
"""
Make a phone call via Twilio
----------------------------
Env vars: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM, TWILIO_TO
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
    call = client.calls.create(
        twiml='<Response><Say>Hello, this is a Python test call!</Say></Response>',
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
    print("Call started, SID:", call.sid)

if __name__ == "__main__":
    main()
