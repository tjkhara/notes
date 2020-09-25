# try
# except
# else
# finally

while True:

	try:
		num = int(input("Please enter a number: "))
	except ValueError: # This runs when there is a problem
		print("That's not a number")
	else: # This runs when there is no problem
		print("Good job you entered a number")
		break
	finally: # This will run no matter what
		print("Runs no matter what")

print("Rest of the game logic runs.")
