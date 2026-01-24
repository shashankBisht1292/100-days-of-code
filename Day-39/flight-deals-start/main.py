#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_sheet_data()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        iata_code = flight_search.get_iata_code(row["city"])
        pprint(f"{row["id"]} - {iata_code}")
        data_manager.update_iata_code(row["id"], iata_code)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for row in sheet_data:
    print(f"Getting flights for {row["city"]}...")
    flights = flight_search.get_flight_prices(origin_city_code= ORIGIN_CITY_IATA, destination_city_code=row["iataCode"], from_time=tomorrow, to_time=six_month_from_today)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"cheapest_flight : {cheapest_flight.price}")
    print(f"my price : {row["lowestPrice"]}")
    if cheapest_flight.price != "N/A" and cheapest_flight.price < row["lowestPrice"]:
        print(f"Lower price flight found to {row['city']}!")
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )