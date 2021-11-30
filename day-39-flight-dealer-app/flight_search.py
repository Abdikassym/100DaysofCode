import requests
from pprint import pprint

API_KEY = "yR1LeaULXWAE3Hfp3k123AbKjHhRSxy8"
API_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {
            "apikey": API_KEY
        }

        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{API_ENDPOINT}/locations/query", params=query, headers=headers)
        code = response.json()["locations"][0]["code"]
        return code


