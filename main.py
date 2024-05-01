import requests
import time
import os
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

# Load environment variables
load_dotenv()
config = dotenv_values(".env")
API_KEY = os.getenv("CRONJOB_API_KEY")
URL = "http://localhost:3000/api/cronjobs"

# Raise an error if the API key is not set
if not API_KEY:
    raise ValueError("CRONJOB_API_KEY environment variable not set")

# Function to send the POST request to the API
def send_api_post():
    headers = {"Authorization": API_KEY}
    data = {}  # Empty body

    try:
        response = requests.post(URL, headers=headers, json=data)
        response.raise_for_status()  
        print(f"API request successful. Status code: {response.status_code}")
        if 'data' in response.json():
            print(f"ID: {response.json()['data'][0]['id']}")
        else:
            print("No data returned in the response")
    except requests.exceptions.RequestException as e:
        print(f"Error sending API request: {e}")

def main():
 
    target_hour = 22
    target_minute = 0  

    while True:
    
        current_time = datetime.now().strftime("%H:%M") 
        target_time = f"{target_hour:02d}:{target_minute:02d}"

       
        if current_time == target_time:
            send_api_post()

        

if __name__ == "__main__":
    main()  
