
"""
Send a WhatsApp message using Twilio Sandbox
-------------------------------------------
1) Join the sandbox in Twilio console to get FROM number like +14155238886
2) Env vars: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, WHATSAPP_FROM, WHATSAPP_TO
pip install twilio
"""
import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "your_account_sid")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "your_auth_token")
WHATSAPP_FROM = os.getenv("WHATSAPP_FROM", "whatsapp:+14155238886")
WHATSAPP_TO = os.getenv("WHATSAPP_TO", "whatsapp:+919876543210")

def main():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Hello, this is a test WhatsApp message from Python!",
        from_=WHATSAPP_FROM,
        to=WHATSAPP_TO
    )
    print("WhatsApp message sent:", message.sid)

if __name__ == "__main__":
    main()
