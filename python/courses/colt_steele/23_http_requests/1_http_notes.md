# HTTP requests

Type in google.com

## This is the request response cycle

1. DNS request - it takes google.com and finds the correct address
2. Computer makes the request to that server
3. Server receives that request and sends them the home page or search results

### DNS Lookup

The phonebook of the internet.

Takes google.com and turns it into an ip address.

Everyone's computer is a client.

The client sends a get request to an ip address.

The server processes the request and maybe checks with a database.

Then sends the data back.

## HTTP Verbs

GET request

* Userful for getting data
* Not setting data
* No side effects
* Can be cached

POST request

* Trying to submit a new comment on Reddit
* Posting photo on Facebook
* Can have side effects
* Cannot be cached

---

## Summary of making a simple request with python

	import requests
	url = "https://icanhazdadjoke.com/"

	# Keep this as is to get back json
	response = requests.get(url, headers={"Accept": "application/json"})

	# This will take the json and turn it into python
	data = response.json()

	print(type(data))

	# so we can now print the joke from this dictionary
	print(data["joke"])

---

## Query String

A way to pass data to a server as a part of a GET request.

	http://www.example.com/?key1=value1&key2=value2

A way to send data to a server to give more information about a particular request.

The & signs join these together