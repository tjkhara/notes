import requests

# This is how you send a get request
response = requests.get("https://news.ycombinator.com")

print(response)

print(response.ok)

print(response.headers)

# This is the main thing
# This is the same thing as viewing the source of the page
print(response.text)