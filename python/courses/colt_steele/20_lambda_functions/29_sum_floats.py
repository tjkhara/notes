def sum_floats(*args):
	return sum(num for num in args if isinstance(num, float))

print(sum_floats(1.0,2,3.0,4))


# list comp reference
# numbers = list(range(1,10))

# evens = [num for num in numbers if num % 2 == 0]