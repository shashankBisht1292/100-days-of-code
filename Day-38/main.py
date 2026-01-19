import requests
from datetime import datetime
import os

API_HEADERS = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "Content-Type": "application/json",
}
BASE_URL = "https://app.100daysofpython.dev"
SHEETY_URL = os.getenv("SHEET_ENDPOINT")

nutrition_url = f"{BASE_URL}/v1/nutrition/natural/exercise"
user_workout_txt = input("Tell me which exercises you did: ").split("and")
for user_workout in user_workout_txt:
    exercise_params = {
        "query": user_workout.strip()
    }
    nutrition_response = requests.post(nutrition_url, headers=API_HEADERS, json=exercise_params)
    nutrition_response.raise_for_status()
    exercise = nutrition_response.json()["exercises"][0]

    today = datetime.now()
    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheety_response = requests.post(SHEETY_URL, headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('TOKEN')}"
    }, json=sheety_params)
