def add_and_multiply_numbers(a,b,c):
	return a + b * c

data = dict(a=1,b=2,c=3)

print(add_and_multiply_numbers(**data))