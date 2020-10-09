import requests

payload = {
	'username': 'tkhara',
	'password': 'testing'
}
r = requests.post('http://www.httpbin.org/post', data=payload)

print(r.text)

