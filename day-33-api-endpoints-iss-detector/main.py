import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 43.228273  # Your latitude
MY_LONG = 76.912110  # Your longitude
ACCEPTABLE_LAT = range(int(MY_LAT) - 5, int(MY_LAT) + 5)
ACCEPTABLE_LONG = range(int(MY_LONG) - 5, int(MY_LONG) + 5)


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude in ACCEPTABLE_LAT and iss_longitude in ACCEPTABLE_LONG:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    global current_hours
    current_hours = datetime.now()
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if current_hours.hour <= sunrise or current_hours.hour >= sunset:
        return True


def is_iss_visible():
    if is_night() == is_iss_overhead():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="abdikasymt@yahoo.com", password="kyeqcnsinwqqtlog")
            connection.sendmail(to_addrs="abdikasymt@gmail.com",
                                from_addr="abdikasymt@yahoo.com",
                                msg="Subject:Is ISS Above?\n\nLook up! There is an ISS above your house!")
            print("ISS! Look above!")
    else:
        print(f"No ISS at {current_hours.time()}")


while True:
    is_iss_visible()
    time.sleep(180)

