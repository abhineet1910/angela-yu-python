import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USER_ENDPOINT = os.environ["SHEETY_USER_ENDPOINT"]
class DataManager:

    def __init__(self):
        self.API_KEY = os.getenv("SHEETY_KEY")
        self.SHEETY_URL = os.getenv("SHEETY_PRICES_ENDPOINT")
        self.SHEETY_USER_URL = os.getenv("SHEETY_USER_ENDPOINT")
        self.sheety_header = {
            "Authorization": self.API_KEY
        }
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheety_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.sheety_header
        )
    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USER_ENDPOINT, headers=self.sheety_header)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data



