
"""
Menu-driven console app to run different automation tasks.
----------------------------------------------------------
This menu prints instructions and points you to the correct script.
You can plug function calls directly if you prefer a single file.
"""
import os
import subprocess
import sys

SCRIPTS = [
    "send_email_smtp_gmail.py",
    "send_sms_twilio_basic.py",
    "make_phone_call_twilio_demo.py",
    "post_linkedin_v2_ugc.py",
    "post_twitter_x_tweepy_v2.py",
    "post_facebook_graph_api.py",
    "post_instagram_graph_api_basic.py",
    "send_whatsapp_twilio_sandbox.py",
]

def pick(idx):
    if 1 <= idx <= len(SCRIPTS):
        script = SCRIPTS[idx-1]
        print(f"Running: {script}\n")
        subprocess.run([sys.executable, script], check=False)
    else:
        print("Invalid choice.")

def main():
    while True:
        print("\n=== Python Automation Menu ===")
        for i, s in enumerate(SCRIPTS, 1):
            print(f"{i}. {s}")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "9":
            print("Exiting...")
            break
        if choice.isdigit():
            pick(int(choice))
        else:
            print("Please enter a number.")

if __name__ == "__main__":
    main()
