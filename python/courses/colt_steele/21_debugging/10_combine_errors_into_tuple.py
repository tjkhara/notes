def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}") 

print(divide(1,2))

print(divide(1,0))

print(divide(1,'a'))