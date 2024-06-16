import requests
from datetime import datetime
import smtplib

MY_LAT = 13.082680
MY_LNG = 80.270721
MY_EMAIL = "sanjalaramesh27@gmail.com"
MY_PW = "dzhiokivexmktdiq"


def check_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    # print(sunrise, sunset)

    now = datetime.now()
    # print(now.hour)
    if int(sunrise) >= now.hour or int(sunset) <= now.hour:
        return True


def pos():
    resp = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(resp)

    # response codes: 1xx (Hold on), 2xx (Here you go), 3xx (Go away), 4xx (You screwed up), 5xx (I screwed up)

    # if response.status_code == 400:
    #     raise Exception("That resource does not exist")
    resp.raise_for_status()

    iss_data = resp.json()
    # print(data["iss_position"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    # print(iss_longitude, iss_latitude)

    if iss_latitude in range(int(MY_LAT - 5), int(MY_LAT + 5)) and iss_longitude in range(int(MY_LNG - 5),
                                                                                          int(MY_LNG + 5)):
        return True


if pos() and check_time():
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=MY_EMAIL, password=MY_PW)
        conn.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="126158046@sastra.ac.in",
            msg="Subject:Look up\n\nThe ISS is above you!"
        )
