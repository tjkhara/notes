def sum_even_values(*args):
	evens = [num for num in args if num % 2 ==0]
	if len(evens) == 0:
		return 0
	else:
		sum_evens = sum(evens)
		return sum_evens


print(sum_even_values(1,2,3,4))


# list comp reference

# numbers = list(range(1,10))

# evens = [num for num in numbers if num % 2 == 0]