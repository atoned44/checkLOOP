import os
import requests
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)

# Pushsafer API configuration
PUSHSAFER_URL = "https://www.pushsafer.com/api"
pushsafer_access_key = os.environ.get("PUSHSAFER_ACCESS_KEY")

if not pushsafer_access_key:
    logging.error("PUSHSAFER_ACCESS_KEY is not set. Check your GitHub Secrets.")
    exit(1)

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
        logging.info(f"Sending notification with payload: {payload}")
        response = requests.post(PUSHSAFER_URL, data=payload, timeout=10)
        logging.info(f"Pushsafer API response: {response.status_code} - {response.text}")

        if response.status_code == 200:
            logging.info(f"Notification sent successfully at {datetime.now()}")
        else:
            logging.error(f"Failed to send notification: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error occurred while sending notification: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

<!-- 
if __name__ == "__main__":
    send_notification() 
-->
