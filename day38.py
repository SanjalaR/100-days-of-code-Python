import requests
from datetime import datetime

GENDER = 'female'
WEIGHT = '49'
HEIGHT = '160'
AGE = '20'
text = input('Tell me which exercises you did: ')
header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}
parameters = {
    'query': text,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}
response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', headers=header, json=parameters)
print(response.json())
response = response.json()
addurl = 'https://api.sheety.co/7795a6f544fe38d75199e77aa1418014/myWorkouts/workouts'

for ex in response['exercises']:
    exercise = ex['name']
    dur = ex['duration_min']
    cal = ex['nf_calories']
    date = datetime.now().strftime(format='%d/%m/%Y')
    time = datetime.now().strftime(format='%I:%M:%S')
    parameters2 = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise.title(),
            'duration': dur,
            'calories': cal,
        }
    }
    auth = (
        '',
        '',
    )
    response2 = requests.post(url=addurl, json=parameters2,  auth=auth)
    print(response2.text)
