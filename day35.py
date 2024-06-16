key = "c5d5969595fe8d623130c03a5627e6e8"
lat = 13.072090
long = 80.201859
code = "4MME4SYHB473Z7WL2R9XYUYA"

import requests
from twilio.rest import Client

parameters = {
    "lat": lat,
    "lon": long,
    "appid": key,
    "cnt": 4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
# print(type(data))
# print(data['weather'])
# weather_id = data['weather'][0]['id']
# weather_desc = data['weather'][0]['description']
# print(weather_id, weather_desc)
data_list = data['list']

account_sid = ACC_S_ID
auth_token = TOKEN

rain = False
for i in data_list:
    weather_id = i['weather'][0]['id']
    print(weather_id)
    if weather_id < 700:
        rain = True
if rain:
    print('Bring an umbrella!')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's gonna rain today! Bring an Umbrella! ☂️",
        from_='+13365375389',
        to='+916380971674'
    )
    print(message.status)


