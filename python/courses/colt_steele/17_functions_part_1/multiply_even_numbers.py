'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''

def multiply_even_numbers(list_in):
	result = 1
	for x in list_in:
		if x % 2 == 0:
			result = result * x
	return result

list_in = list(range(2,7))

y = multiply_even_numbers(list_in)

print(y)

    