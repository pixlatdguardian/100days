import requests
from datetime import datetime

MY_LAT = 45.0 # Your latitude
MY_LONG = -122.0  # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "tzid": "America/Vancouver",
    "formatted": 0,
}


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour <= sunrise:
        return True


# If the ISS is close to my current position

if iss_overhead() and is_dark():
    print("ISS overhead")
else:
    print("Not overhead")


# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.