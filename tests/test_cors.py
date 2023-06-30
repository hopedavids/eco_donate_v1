import requests
from bs4 import BeautifulSoup

# Example GET request
url = 'http://172.18.0.2:5000/transaction'
response = requests.get(url)


with open('response.html', 'wb') as file:
        file.write(response.content)

with open('response.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Example: Check for "Access-Control-Allow-Origin" header in the response
if 'Access-Control-Allow-Origin' in response.headers:
    print("CORS vulnerability found!")
