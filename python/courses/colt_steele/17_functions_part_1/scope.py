# global scope

total = 0

def increment():
	global total 
	total += 1
	return total

increment()
increment()


print(total)