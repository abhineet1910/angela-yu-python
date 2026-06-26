from http.cookiejar import HEADER_VALUE_RE

import requests
import os
import dotenv
from dotenv import load_dotenv
from datetime import datetime

GENDER = "male"
AGE = 22
WEIGHT_KG = 75
HEIGHT = 175
EXERCISE = input("Tell me which exercise you did\nExercise description eg(ran for 30 minutes,swam for 1 hour) :")

load_dotenv()
try:
    APP_ID = os.getenv("YOUR_APP_ID")
    # get your own appid at :https://app.100daysofpython.dev
    API_KEY = os.getenv("YOUR_API_KEY")
    # get your own apikey at :https://app.100daysofpython.dev
    SHEETY_ENDPOINT = os.getenv("YOUR_SHEETY_ENDPOINT")
    # gey your endpoint at :https://dashboard.sheety.co
    SHEETY_TOKEN = os.getenv("YOUR_SHEETY_APIKEY")
    # gey your apikey at :https://dashboard.sheety.co
    WORKOUT_TRACKER_ENDPOINT = os.getenv("WORKOUT_TRAKER_URL")
    # get your own workout traker api url at :https://app.100daysofpython.dev
    if None in (
            APP_ID,
            API_KEY,
            SHEETY_ENDPOINT,
            SHEETY_TOKEN,
            WORKOUT_TRACKER_ENDPOINT,
    ):
        raise ValueError("Missing environment variables.")

except ValueError as e:
    print(f"Error: {e}")


harder = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}


traker_url = WORKOUT_TRACKER_ENDPOINT

params = {
    "query":EXERCISE,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT,
    "age":AGE,
    "gender": GENDER

}
response = requests.post(url=traker_url,
                         json=params,
                         headers=harder)

print(response.text)
results = response.json()
print(results["exercises"][0])


sheety_url = SHEETY_ENDPOINT
sheety_header={
    "Authorization": SHEETY_TOKEN
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#
for exercise in results["exercises"]:
    sheet_input ={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],

        }
    }
    sheet_response = requests.post(sheety_url, json=sheet_input, headers=sheety_header)

    print(sheet_response.text)









