from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_params = {
            "grant_type": "client_credentials",
            "client_id": os.environ["AMADEUS_API_KEY"],
            "client_secret": os.environ["AMADEUS_SPI_SECRET"],
        }
        token_response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", data=token_params, headers=token_headers)
        token_response.raise_for_status()
        return token_response.json()["access_token"]

    def get_iata_code(self, city_name):
        iata_code_headers = {
            "Authorization": f"Bearer {self._token}",
        }
        iata_code_params = {
            "keyword": city_name
        }
        iata_code_response = requests.get("https://test.api.amadeus.com/v1/reference-data/locations/cities", params=iata_code_params, headers=iata_code_headers)
        iata_code_response.raise_for_status()
        return iata_code_response.json()["data"][0]["iataCode"]

    def get_flight_prices(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        parms = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get("https://test.api.amadeus.com/v2/shopping/flight-offers", params=parms, headers=headers)
        response.raise_for_status()
        return response.json()