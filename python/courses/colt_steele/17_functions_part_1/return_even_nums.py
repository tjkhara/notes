def generate_evens():
	return [x for x in range(1,49) if x % 2 == 0]

print(generate_evens())