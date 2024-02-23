import requests

parameters = {
    "lat": 45.559106,
    "lon": -122.665252,
    "appid": "apikey",
    "units": "imperial",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()
weather_data = response.json()

for entry in weather_data["list"]:
    rain = False
    if entry["weather"][0]["id"] < 700:
        rain = True
    else:
        pass
    if rain:
        print("Bring an umbrella")