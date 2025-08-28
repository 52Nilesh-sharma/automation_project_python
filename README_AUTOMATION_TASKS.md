
# Python Automation Pack

A collection of small Python scripts to complete your assignment tasks:
- Send Email
- Send SMS (Twilio)
- Make a Phone Call (Twilio)
- Post on LinkedIn
- Post on X (Twitter)
- Post on Facebook
- Post on Instagram
- Send WhatsApp (Twilio)
- Menu-driven launcher

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Variables

Export the variables needed for the scripts you run. Examples:

```bash
# Gmail SMTP
export SENDER_EMAIL="your_email@gmail.com"
export APP_PASSWORD="your_app_password"
export RECEIVER_EMAIL="receiver@example.com"

# Twilio
export TWILIO_ACCOUNT_SID="ACxxxx"
export TWILIO_AUTH_TOKEN="xxxx"
export TWILIO_FROM="+1xxx"
export TWILIO_TO="+91xxxxxxxxxx"
export WHATSAPP_FROM="whatsapp:+14155238886"
export WHATSAPP_TO="whatsapp:+91xxxxxxxxxx"

# LinkedIn
export LINKEDIN_ACCESS_TOKEN="xxxx"
export LINKEDIN_AUTHOR_URN="urn:li:person:xxxxxxxx"

# Twitter (X)
export TWITTER_API_KEY="xxxx"
export TWITTER_API_SECRET="xxxx"
export TWITTER_ACCESS_TOKEN="xxxx"
export TWITTER_ACCESS_SECRET="xxxx"

# Facebook Page
export FB_PAGE_ACCESS_TOKEN="xxxx"
export FB_PAGE_ID="1234567890"

# Instagram Graph API
export IG_ACCESS_TOKEN="xxxx"
export IG_BUSINESS_ID="1789xxxxxxxx"
export IMAGE_URL="https://www.python.org/static/community_logos/python-logo.png"
export CAPTION="Hello Instagram! 🚀"
```

## Run

```bash
python automation_menu_all_tasks.py
```

Or run any individual script with:

```bash
python send_email_smtp_gmail.py
```

## Notes
- Replace placeholders or use environment variables.
- For LinkedIn/Twitter/Facebook/Instagram, you must have developer access and valid tokens.
- For Gmail, use an App Password (with 2FA enabled).
