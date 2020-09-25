users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#extract inactive users using list comprehension:
inactive_users = [d for d in users if len(d.get("tweets")) == 0]

print(inactive_users)


# example
# evens = [num for num in numbers if num % 2 == 0]