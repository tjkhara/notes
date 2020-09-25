users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# extract usernames of inactive users w/ map and filter:

# let's try to make a new list with map where all the users have no tweets

# first filter the users who are inactive
inactive_users = list(filter(lambda x : len(x.get("tweets")) == 0, users))

# now use map to extract usernames
user_names = list(map(lambda d:d["username"], inactive_users))

print(user_names)



# example
# first_names = list(map(lambda d:d["first"], names))