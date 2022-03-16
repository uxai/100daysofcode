import requests
from datetime import datetime as dt

NUTRITIONIX_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
G_SHEET_GET = ""
G_SHEET_POST = ""

SHEETY_TOKEN = ""

sheety_headers =  {
    'Authorization': f"Bearer {SHEETY_TOKEN}"
}

nix_headers = {
    'x-app-id': "",
    'x-app-key': ""
    # x-remote-user-id: 0
}

nix_params = {
    'gender': "male",
    'weight_kg': 90,
    'height_cm': 180,
    'age': 33
}

workout = input("Tell me what workout you did today: ")

nix_query = {
    'query': workout
}

response = requests.post(url=NUTRITIONIX_EP, json=nix_params, data=nix_query, headers=nix_headers)
exercise_stats = response.json()['exercises']

date = dt.now()

body = {
    'workout': {
        'date': date.strftime("%Y%m%d"),
        'time': date.strftime("%H:%M")
    }
}

for stat in exercise_stats:
    body['workout']['exercise'] = stat['name']
    body['workout']['duration'] = stat['duration_min']
    body['workout']['calories'] = stat['nf_calories']
    workout_res = requests.post(url=G_SHEET_POST, json=body, headers=sheety_headers)
    print(workout_res.text)