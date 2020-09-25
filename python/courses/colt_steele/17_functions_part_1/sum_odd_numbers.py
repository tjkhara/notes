l1 = list(range(1,20))

# how to sum the odd numbers in this list

def sum_odd_nums(list_in):
	sum = 0
	for x in list_in:
		if x % 2 == 1:
			sum += x

	return sum

print(sum_odd_nums(l1))