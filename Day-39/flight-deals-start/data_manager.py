import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
       self.get_url = "https://api.sheety.co/73d5b48f5661e02e3bba713818a8bde9/myFlightDeals/prices"
       self.put_url = "https://api.sheety.co/73d5b48f5661e02e3bba713818a8bde9/myFlightDeals/prices/[Object ID]"
       self.sheety_headers = {
           "Authorization": f"Bearer {os.getenv('SHEETY_TOKEN')}"
       }

    def get_sheet_data(self):
        get_sheety_response = requests.get(self.get_url, headers=self.sheety_headers)
        get_sheety_response.raise_for_status()
        return get_sheety_response.json()["prices"]

    def update_iata_code(self, id, iata_code):
        update_sheety_params = {
            "price": {
               "iataCode": iata_code
            }
        }
        update_sheety_response = requests.put(self.put_url.replace("[Object ID]", str(id)), json=update_sheety_params, headers=self.sheety_headers)
        update_sheety_response.raise_for_status()
        print(update_sheety_response.json())

