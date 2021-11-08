import requests

parameters = {
    "type": "boolean",
    "amount": 10,
    "formatted": 0
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions = response.json()
question_data = questions["results"]
