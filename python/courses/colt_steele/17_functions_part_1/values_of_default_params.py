def add(a,b):
	return a+b

# the fn function defaults to add, but you can send in anything
def math(a,b, fn=add):
	return fn(a,b)

def subtract(a,b):
	return a - b

x = math(2,1,subtract)
print(x)