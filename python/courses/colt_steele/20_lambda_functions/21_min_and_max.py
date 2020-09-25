# Example 1

# print(max(3,77,99))

# Can pass in an iterable as well

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

print(min(names)) # Arya

print(max(names)) # Tim

# This is a list comprehension but we can use it as a generator expression and leave the [] out
print(min(len(name) for name in names))

# to get the name back we use a lambda

print(max(names, key=lambda n:len(n))) # Ollivander

print(min(names, key=lambda n:len(n))) # Tim


# --------------------------------------------------------------------------------------------------------

# Another example

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Find songs with lowest playercount

print(min(songs, key=lambda song:song["playcount"])) # Tim

