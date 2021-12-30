import requests
MY_LAT = "-5.429750"
MY_LNG = "105.262268"
current = "current"
minutely = "minutely"
hourly = "hourly"
daily = "daily"
alerts = "alerts"
api_key = "cde3aed6ead21fea067c6db611474f24"


weather = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}&exclude={alerts}&appid={api_key}")
weather.raise_for_status()
json_data = weather.json()
print(json_data)
