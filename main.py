import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=url)
name = input()
users = response.json()

for user in users:
    if name == user["name"]:
        print(print(f"User ID: {user['id']} | Website: {user['website']}"))