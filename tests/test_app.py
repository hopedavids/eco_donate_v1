import requests


""" This script is primarily to test the api endpoints and HTTP methods """

url = 'http://0.0.0.0:5000/'

response = requests.get(url + '/auth_user')


print(response.status_code)
print(response.headers)
print(response.text)
print(response.json())