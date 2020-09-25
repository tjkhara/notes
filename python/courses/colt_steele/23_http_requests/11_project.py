
topic = input("Let me tell you a joke. Give me a topic!")

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": topic}
)

data = response.json()
# print(data)
if not data['total_jokes']:
	print("Sorry no jokes about that!")
else:
	print(f"I've got {data['total_jokes']} jokes about {topic}s here's one:")
	# print(data["results"][0]["joke"])

	# pick a joke at random
	from random import choice

	c = choice(data["results"])

	print(c['joke'])