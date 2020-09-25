
def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1


# this is using a generator function to quickly create an iterator
counter = count_up_to(10)

# looping through the iterator
for num in counter:
	print(num)

