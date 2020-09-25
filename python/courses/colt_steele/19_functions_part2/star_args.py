def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num
	return total

print(sum_all_nums(1,2,3,4,5))
print(sum_all_nums(100,200))