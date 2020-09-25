

for x in range(1,21):
	
	print(f"x is {x}")

	if x == 4 or x == 13:
		print("x is unlucky")
	elif x % 2 == 0:
		print("x is even")
	else:
		print("x is odd")