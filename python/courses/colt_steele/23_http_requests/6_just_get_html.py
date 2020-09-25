import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url)

print(response.text)