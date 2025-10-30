import requests
import os

token = os.environ['github_access_token']

username = input("Enter Username: ")

BASE_URL = "https://api.github.com"

headers={
    'Authorization':f'token {token}',
    "Accept":"application/vnd.github.v3+json"
}

url = f"{BASE_URL}/users/{username}/events"
response = requests.get(url, headers=headers)
events = response.json()

for e in events[:5]:
    print(f"{e['type']} on {e['repo']['name']} at {e['created_at']}")
