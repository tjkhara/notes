# Decrators are functions that wrap other functions

def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a great day!")
	return wrapper



def greet():
	print("My name is Colt.")

def rage():
	print("I hate you.")

# greet()
g = be_polite(greet)
g()

r = be_polite(rage)
r()