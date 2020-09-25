# Generator expressions

def nums():
	for num in range(1,10):
		yield num

g = nums()


# for x in range(9):
# 	print(next(g))

# shortcut to do the same thing

g = (num for num in range(1,10))

for x in range(9):
	print(next(g))