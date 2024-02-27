import requests
import datetime

API_KEY = "apikey"
APP_ID = "appid"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/{sheet data}"

GENDER = "male"
WEIGHT_KG = str(190 * 0.453)
HEIGHT_CM = str(175)
AGE = str(31)

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query" : input("What did you do today?"),
    "gender" : GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age": AGE,

}

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
data = response.json()

time_now = datetime.datetime.now()

for exercise in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": time_now.strftime("%m-%d-%Y"),
            "time": time_now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    post = requests.post(sheet_endpoint, json=sheet_inputs)