import os
from dotenv import load_dotenv
from urllib import response

from twilio.rest import Client
import requests
from urllib3.util import url
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
apikey = os.getenv("OPENWEATHER_API_KEY")


parameters = {
    "lat":21.213779,
    "lon":81.344757,
    "appid":apikey,
    "cnt":4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?",params=parameters)
print(response.status_code )
response.raise_for_status()
data = response.json()
weather_today = data['list'][0]['weather'][0]['id']
will_rain = False
for forecast in data['list']:
    weather_id = forecast['weather'][0]['id']
    time = forecast['dt_txt']
    time_part = time.split(" ")[1]
    hour = time_part.split(":")[0]
    if int(weather_id) < 700:
        will_rain = True

    # weather = forecast['weather'][0]['main']
    # print(F" WAETHER ID :{weather_id},CONDITON :{weather} at :{hour} o clock")
    # if weather_id < 700:
    #     print(f"☔ Rain/Snow expected at {hour} o clock")
    #
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="there is going to rain today! be wet and cool ⛈️🌦️🌧️☂️.",
        from_="+19283930299",
        to="+918770769388",
    )
    print(message.status)
    print(message.sid)

