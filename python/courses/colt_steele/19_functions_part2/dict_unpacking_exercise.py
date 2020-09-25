'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate(make_float, operation, first, second, message="The result is"):
	initial_result = None

	if operation == 'add':
		initial_result = first + second
	if operation == 'subtract':
		initial_result = first - second
	if operation == "multiply":
		initial_result = first * second
	if operation == "divide":
		initial_result = first/second

	if message:
		if make_float:
			return f"{message} {float(initial_result)}"
		else:
			return f"{message} {initial_result}"
	else:
		if make_float:
			return f"{message} {float(initial_result)}"
		else:
			return f"{message} {initial_result}"


x = calculate(make_float=False, operation='add', message='You just added', first=2, second=4)

print(x)

y = calculate(make_float=True, operation='divide', first=3.5, second=5)

print(y) 