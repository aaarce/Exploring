# Task: Fetch data from a public API
import requests
import json


url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
data = response.json()  # Convert JSON response into Python dictionary

# Display first post title and second body
print(data[0]['title'])
print(data[1]['body'])