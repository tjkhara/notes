# if you have a function in a function then you can use non local to access the outer function's variables inside the
# inner function for modification

def outer():
	count = 0
	def inner():
		nonlocal count
		count += 1
		return count
	return inner()