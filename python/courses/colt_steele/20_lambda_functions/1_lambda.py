# normal function call
def square(num):
	return num ** 2

print(square(9))

# lambda

square2 = lambda num: num ** 2

# how to call this?
print(square2(9))

# another lambda

add = lambda a,b: a + b

print(add(3,10))

# how to check if the lambda has a name?

print(square.__name__)

print(square2.__name__)

print(add.__name__)

# use case
# passing function as a parameter into another function
# and we wont use it again