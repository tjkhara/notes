import requests

params = {
	"key1" : "value1",
	"key2" : "value2"
}

response = requests.get("http://www.example.com", params)

# or it can be written like this

response = requests.get("http://www.example.com", params = {
	"key1" : "value1",
	"key2" : "value2"
})