import os
import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# Pushsafer API configuration
PUSHSAFER_URL = "https://www.pushsafer.com/api"
pushsafer_access_key = os.environ.get("PUSHSAFER_ACCESS_KEY")

def send_notification():
    """
    Send a notification to Pushsafer.
    """
    payload = {
        "k": pushsafer_access_key,
        "m": "Check the Loop app!",
        "t": "Reminder",
        "s": "0"  # Sound (optional)
    }

    try:
        response = requests.post(PUSHSAFER_URL, data=payload)
        if response.status_code == 200:
            logging.info(f"Notification sent successfully at {datetime.now()}")
        else:
            logging.error(f"Failed to send notification: {response.text}")
    except Exception as e:
        logging.error(f"Error occurred while sending notification: {e}")

if __name__ == "__main__":
    send_notification()
