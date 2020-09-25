class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	# getter
	@property
	def age(self):
		return self._age

	# setter
	@age.setter
	def age(self, value):
		# we can do a check here
		if value >= 0:
			self._age = value
		else:
			raise ValueError("age should be greater than 0")

	# getter for full name
	@property
	def full_name(self):
		return f"{self.first} {self.last}"
	


jane = Human("Jane", "Goodall", 50)

# getter usage
# note that we do not need () after age even though age is a method
print(jane.age)

# The problem is that someone can set the value of a property from the outside to a bogus value
# jane.age = -100

# set value using the setter
jane.age = 20

print(jane.age)

# trying a bogus value
# jane.age = -10

# trying full name
print(jane.full_name)

# dunder dict
print(jane.__dict__)


	
	