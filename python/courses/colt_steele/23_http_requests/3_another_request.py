import requests

url = "http://www.google.com"

# This is how you send a get request
response = requests.get(url)

print(f"your request to {url} came back with status code {response.status_code}")