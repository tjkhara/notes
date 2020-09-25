# we can pass a function as an argument to another function

def sum(n, func):
	total = 0

	for num in range(1,n+1):
		total += func(num)

	return total


def square(x):
	return x*x

def cube(x):
	return x**3

print(sum(10,square))

print(sum(10,cube))