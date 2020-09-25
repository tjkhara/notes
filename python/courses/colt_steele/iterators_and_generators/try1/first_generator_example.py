
def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1


x = count_up_to(10)

print(next(x)) # 1
print(next(x)) # 2

help(x)