def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

l1 = [1,2,3,4,5,6]

# this * in the argument means that we are sending in all the values in the list as arguments

print(sum_all_nums(*l1))