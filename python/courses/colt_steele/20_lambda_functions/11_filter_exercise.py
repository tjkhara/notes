def remove_negatives(list_in):
	return list(filter(lambda x:x>=0, list_in))


# for reference filter example
# evens = list(filter(lambda x: x % 2 == 0, l))

dl = remove_negatives([-1,-2,4,5])

print(dl)