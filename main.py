import requests
import time
import os

from dotenv import load_dotenv, dotenv_values

# Load API key from environment variable
load_dotenv()
config = dotenv_values(".env")
API_KEY = os.getenv("CRONJOB_API_KEY")
URL = "http://localhost:3000/api/cronjobs"

if not API_KEY:
    raise ValueError("CRONJOB_API_KEY environment variable not set")


def send_api_post():
    headers = {"Authorization": API_KEY}
    data = {}  # Empty body

    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for non-2xx status codes
        print(f"API request successful. Status code: {response.status_code}")
        print(f"ID: {response.json()['data'][0]['id']}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending API request: {e}")


if __name__ == "__main__":
    while True:
        send_api_post()
        time.sleep(10)  # Sleep for 20 seconds
