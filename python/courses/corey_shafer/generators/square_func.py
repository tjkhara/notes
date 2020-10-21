# From this video
# https://www.youtube.com/watch?v=bD05uGo_sVI

# This is how you would do this using a function

def square_func(list_in):
	result = []
	for num in list_in:
		result.append(num ** 2)
	return result

list_1 = [1,2,3,4,5]

list_2 = square_func(list_1)

# print(list_2)

# This is using a generator function

def square_numbers(nums):
	for i in nums:
		yield(i**2)

x = square_numbers([1,2,3,4,5])

# print(next(x))
# print(next(x))

# We can use a for loop in these generators as well
# You can use a for loop on the generator

# for n in x:
	# print(n)

# We can write this generator as a list comprehension as well

# list_of_nums = [1,2,3,4,5,6]

# y = [n**2 for n in list_of_nums]

# for value in y:
# 	print(value)

# This is how you write a generator expression just replace the [] with ()

list_of_nums = [1,2,3,4,5,6]

y = (n**2 for n in list_of_nums)

# for value in y:
	# print(value)

# you can take a generator object and convert it to a list as well

square_list = list(y)

print(square_list)