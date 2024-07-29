import requests
from datetime import datetime
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

API_KEY = os.getenv('NUTRITIONIX_API')
ID_KEY = os.getenv('NUTRITIONIX_ID')
MY_WORKOUT_TOKEN = os.getenv('MY_WORKOUT_TOKEN')

GENDER = 'Male'
WEIGHT_KG = '61'
HEIGHT_CM = '168'
AGE = '26'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": ID_KEY,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response_nutrition = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response_nutrition.json()
Exercise = result['exercises'][0]['user_input'].title()
Duration = result['exercises'][0]['duration_min']
Calories = result['exercises'][0]['nf_calories']


now = datetime.now()
now_time = now.time()

URL = 'https://api.sheety.co/dfeb845ae19c4c45169cac46b21c9926/myWorkouts/workouts'

params = {'workout':
          {'date':now.strftime("%m/%d/%Y"),
           'time':now_time.strftime('%H:%M:%S'),
           'exercise': Exercise,
           'duration': Duration,
           'calories': Calories}
          }

headers = {"Authorization": f"Bearer {MY_WORKOUT_TOKEN}"}

response = requests.post(URL,json=params, headers=headers)
