import requests

DATA_ENDPOINT = "https://api.sheety.co/e01336d82c10580faffe1112e877f18c/flights/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=DATA_ENDPOINT).json()
        self.destination_data = response["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_body = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{DATA_ENDPOINT}/{city['id']}", json=new_body)
