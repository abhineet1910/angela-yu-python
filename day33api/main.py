
# architecture
# my position is +5,-5 degree of the iss position
# change is to spot the isss at night
# if the iss is at my location
# & if its dark out side means time after lets
# assume time between after sunset and before sun rise
# then send me the email



import datetime as dt
import smtplib
import requests
import time
my_email = "testingmail1910@gmail.com"
my_password = "pgvihylddsxwxqyb"

my_lat = 21.213782
my_long = 81.344756

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response)
    # print(response.headers)
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    print(iss_position)
    if my_lat-5 <= latitude <= my_lat+5 and my_long-5 <= longitude <= my_long+5:
        return True


parameters ={
    "lat":my_lat,
    "lng":my_long,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



if is_iss_overhead():
    print("look up ")
def is_night():

    time_now = dt.datetime.now()

    current_hour = time_now.hour

    return current_hour >= sunset or current_hour <= sunrise
# if is_night():
#     print("to dark 👻")

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        print("look up iss is over head overhead")
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,to_addrs="codinglord1227@gmail.com",
                            msg="Subject: Look up iss (satelite) is over head overhead")
