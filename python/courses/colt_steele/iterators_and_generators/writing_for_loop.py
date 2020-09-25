# Custom for loop

# def for_loop(input_iterable):
# 	it = iter(input_iterable)
# 	while(True):
# 		try:
# 			print(next(it))
# 		except Exception as e:
# 			raise e


# iterable = [1,2,3,4,5]

# for_loop(iterable)


def my_for(iterable, func):
	iterator = iter(iterable)
	while(True):
		try:
			thing = next(iterator)
		except StopIteration:
			# print("End of iterator")
			break
		else:
			func(thing)


def square(x):
	print(x*x)



my_for([1,2,3,4], squar)e