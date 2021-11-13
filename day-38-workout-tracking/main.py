import requests
from requests.auth import HTTPBasicAuth
import datetime as dt

today = dt.datetime.now().today().strftime("%d/%m/%Y")
current_time = dt.datetime.now().time().strftime("%H:%M:%S")

today_exercises = input("What were you doing today?\n")

API_ID = "233b46c0"
API_KEY = "8674d40b17cfcba973bd9781359555b8"
SHEETY_ENDPOINT = "https://api.sheety.co/63627b957e7f2d071eb225065a64ab46/копияMyWorkouts/workouts"
USERNAME = "pixu"
PASSWORD = "enderman007"

nutritionix_url = "https://trackapi.nutritionix.com"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": today_exercises
}

exercises_endpoint = f"{nutritionix_url}/v2/natural/exercise"
response = requests.post(url=exercises_endpoint, headers=headers, json=exercise_config)

exercises = response.json()["exercises"]

for i in exercises:
    sheety_body = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": i["user_input"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        }
    }

    response_sheety = requests.post(url=SHEETY_ENDPOINT,
                                    json=sheety_body,
                                    auth=HTTPBasicAuth(username=USERNAME, password=PASSWORD))
    print(response_sheety.json())
