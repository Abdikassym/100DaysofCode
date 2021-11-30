import requests
import datetime as dt

starting_time = (dt.datetime.now().today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
ending_time = (dt.datetime.now().today() + dt.timedelta(days=180)).strftime("%d/%m/%Y")

API_KEY = "yR1LeaULXWAE3Hfp3k123AbKjHhRSxy8"
API_ENDPOINT = "https://tequila-api.kiwi.com/v2"
departure_city = "LON"


class FlightData:

    def search_ticket(self, city_to):

        headers = {
            "apikey": API_KEY,
        }

        query = {
            "fly_from": departure_city,
            "fly_to": city_to,
            "flight_type": "round",
            "date_from": starting_time,
            "date_to": ending_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "limit": 1,
            "one_for_city": 1
        }

        response = requests.get(url=f"{API_ENDPOINT}/search", headers=headers, params=query)
        flight_data = response.json()
        return flight_data


