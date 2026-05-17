import random
import requests

FAST2SMS_API_KEY = "YOUR_API_KEY_HERE"

def generate_otp():
    return random.randint(100000, 999999)


def send_otp(phone, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = {
        "route": "otp",
        "variables_values": str(otp),
        "numbers": phone
    }

    headers = {
        "authorization": FAST2SMS_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)  # important for debugging
    return response.json()