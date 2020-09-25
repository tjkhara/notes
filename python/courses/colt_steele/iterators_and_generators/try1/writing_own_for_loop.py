# Custom for loop

num = [1,2,3]


def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
			func(thing)
		except StopIteration:
			break


def square(x):
	print(x*x)

my_for(num, square)	