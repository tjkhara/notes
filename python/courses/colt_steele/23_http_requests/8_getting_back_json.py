import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})

# This will  get back a string
# print(response.text)
# This will take the json and turn it into python
# print(response.json())

# This will return a dictionary
data = response.json()

print(type(data))

# so we can now print the joke from this dictionary
print(data["joke"])
