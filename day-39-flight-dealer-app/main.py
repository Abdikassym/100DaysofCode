from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

DEPARTURE_CITY = "Almaty"
DEPARTURE_CITY_CODE = "ALA"

notification_manager = NotificationManager()
flight_data = FlightData()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()
count = 0
for i in sheet_data:
    count += 1
    try:
        flight = flight_data.search_ticket(i["iataCode"])["data"][0]
        flight_price = flight["price"]
        arrival_city_name = flight["cityTo"]
        arrival_city_code = flight["cityCodeTo"]
        outbound_data = flight["local_departure"][:10]
        inbound_data = flight["route"][-1]["local_departure"][:10]
        print(count, arrival_city_name)
        if flight_price < i["lowestPrice"]:
            print("Nice Price")
            notification_manager.send_message(
                price=flight_price,
                dep_city=DEPARTURE_CITY,
                dep_city_code=DEPARTURE_CITY_CODE,
                arr_city=arrival_city_name,
                arr_city_code=arrival_city_code,
                outbound=outbound_data,
                inbound=inbound_data
            )
    except IndexError:
        continue
