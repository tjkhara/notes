# try
# except
# else
# finally

try:
	num = int(input("Please enter a number: "))
except: # This runs when there is a problem
	print("That's not a number")
else: # This runs when there is no problem
	print("I'm in the else")
finally: # This will run no matter what
	print("Runs no matter what")
