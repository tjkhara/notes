# Decrators are functions that wrap other functions

def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper


@be_polite
def greet():
	print("My name is Colt.")

@be_polite
def rage():
	print("I hate you.")

# now we don't have to do these two lines
# g = be_polite(greet)
# g()

greet()


# r = be_polite(rage)
# r()

rage()