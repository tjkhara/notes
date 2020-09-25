def display_names(first, second):
	return f"{first} says hello to {second}"

# first way to call this function would be
print(display_names(first="Charlie", second="Sue"))

# second way is dictionary unpacking
names = {"first":"Colt", "second":"Rusty"}

print(display_names(**names))