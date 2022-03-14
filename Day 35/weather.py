import requests
import os

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
apikey = os.environ.get("OWM_API")
telkey = os.environ.get("TELE_API")

weather_params = {
    'lat': 1.290270,
    'lon': 103.851959,
    'appid': apikey,
    'exclude': "current,minutely,daily"
}

response = requests.get(endpoint, params=weather_params)
print(response)
response.raise_for_status()
weather_data = response.json()

weather_msg = "It's sunny for the next 12 hours!"
for hour in weather_data['hourly'][:12]:
    if hour['weather'][0]['id'] < 700:
        weather_msg = "Bring an umbrella, it's going to rain!"
        break

telegram_params = {
    'chat_id': 299092252,
    'text': weather_msg
}

tb = requests.post(f"https://api.telegram.org/bot{telkey}/sendMessage", params=telegram_params)
tb.raise_for_status()