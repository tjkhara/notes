import random

def times_table(number):
	x = number
	return_string = ""
	for y in range(1,21):
		return_string += f'\n {number} x {y} = {x*y}\n'
	return return_string

	

z = times_table(14)

print(z)