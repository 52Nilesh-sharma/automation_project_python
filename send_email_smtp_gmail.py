
"""
Send an Email using Python (SMTP over SSL - Gmail example)
---------------------------------------------------------
1) Enable 2FA on your Google account and create an App Password
2) Replace placeholders below or export environment variables:
   - SENDER_EMAIL, APP_PASSWORD, RECEIVER_EMAIL
Usage:
    python send_email_smtp_gmail.py
"""
import os
import smtplib
from email.mime.text import MIMEText

SENDER = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
PASSWORD = os.getenv("APP_PASSWORD", "your_app_password")
RECEIVER = os.getenv("RECEIVER_EMAIL", "receiver@example.com")

SUBJECT = "Python Email Test"
BODY = "Hello, this is a test email sent using Python!"

msg = MIMEText(BODY)
msg['Subject'] = SUBJECT
msg['From'] = SENDER
msg['To'] = RECEIVER

def main():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, PASSWORD)
        server.sendmail(SENDER, [RECEIVER], msg.as_string())
    print("Email sent successfully!")

if __name__ == "__main__":
    main()
