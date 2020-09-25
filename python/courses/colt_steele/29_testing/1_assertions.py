def add_positive_numbers(x,y):
	assert x > 0 and y > 0, "Both numbers must be positive!"
	return x + y

add_positive_numbers(1,1)
add_positive_numbers(1,-1) # This will raise an assertion error

# assert is not a function, but a statement