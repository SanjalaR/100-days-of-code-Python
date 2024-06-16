import requests
from datetime import datetime

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url='https://pixe.la/v1/users', json=parameters)
# print(response.text)

parameters2 = {
    'id': 'graph1',
    'name': 'CODE EVERYDAY!',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': TOKEN,
}
# response2 = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs', json=parameters2, headers=headers)
# print(response2.text)
GRAPHID = 'graph1'

# parameters3 = {
#     'date': '20240527',
#     'quantity': '60',
# }
# response3 = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}', json=parameters3, headers=headers)
# print(response3.text)

today = datetime.now()
parameters4 = {
    'date': today.strftime(format='%Y%m%d'),
    'quantity': '70',
}
# response4 = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}', json=parameters4, headers=headers)
# print(response4.text)

parameters5 = {
    'quantity': '40',
}
# response5 = requests.put(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/20240527', json=parameters5, headers=headers)
# print(response5.text)

# response6 = requests.delete(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}/20240527', headers=headers)
# print(response6.text)

parametersfinal = {
    'date': today.strftime(format='%Y%m%d'),
    'quantity': input('How many minutes did you code today?'),
}
responsefinal = requests.post(url=f'https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPHID}', json=parametersfinal, headers=headers)
print(responsefinal.text)
