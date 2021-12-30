import requests
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
json_data = response.json()
print(json_data)
