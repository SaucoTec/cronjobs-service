import schedule
import time
import requests
import os
from datetime import datetime
from pytz import timezone
from dotenv import load_dotenv, dotenv_values

# Load API key from environment variable
load_dotenv()
config = dotenv_values(".env")
API_KEY = os.getenv("CRONJOB_API_KEY")
URL = "https://app.theringsmethod.com/api/cronjobs"

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

def job():
    # Define timezone
    buenos_aires = timezone('America/Argentina/Buenos_Aires')
    now = datetime.now(buenos_aires)
    print(f"Executing job at {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
    send_api_post()

# Schedule the job every day at 10:30 PM Buenos Aires time
schedule.every().day.at("22:30").do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
