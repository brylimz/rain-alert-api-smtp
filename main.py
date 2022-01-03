import requests
from twilio.rest import Client
account_sid = 'AC80c8050132a9a26a0679fb1ee6a50dfc'
auth_token = '35bc77c83d783397633d9879e1424f14'

MY_LAT = "-5.429750"
MY_LNG = "105.262268"
current = "current"
minutely = "minutely"
hourly = "hourly"
daily = "daily"
alerts = "alerts"

api_key = "cde3aed6ead21fea067c6db611474f24"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going rain today. Remember to bring an umbrella",
        from_='+17605469864',
        to='+6282388444497'
    )

    print(message.status)

# print(json_data["hourly"][0]["weather"][0])

#twilio