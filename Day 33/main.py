import requests
import smtplib
from datetime import datetime as dt
import time

EMAIL = "my_email@gmail.com" # Send email from
PASSWORD = ""
TO_EMAIL = "my_email@gmail.com" # Send notification to

# Offset hours by UTC
TIMEZONE = 8

parameters = {
    'lat': 1.352083,
    'lng': 103.819839,
    'formatted': 0
}

# Get current ISS location from API
response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_lat = float(data['iss_position']['latitude'])
iss_lng = float(data['iss_position']['longitude'])

# Get sunrise/sunset time for specified longitude/latitude
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

print(data['results']['sunrise'])
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0]) + TIMEZONE
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0]) + TIMEZONE

if sunrise > 23:
    sunrise = sunrise - 23
if sunset > 23:
    sunrise = sunrise - 23

current_time = dt.now()
current_hour = current_time.hour

# Print the current Longitude and latitude
while True:
    time.sleep(60)
    print(f"The ISS is currently at: {iss_lat}, {iss_lng}")
    if current_hour >= sunset or current_hour <= sunrise:
        if parameters['lat'] - iss_lat in range(-5, 6) and parameters['lng'] - iss_lng in range(-5, 6):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=TO_EMAIL, msg=f"Subject:Look up! The ISS is overhead\n\nThe ISS is at {iss_lat}, {iss_lng}")