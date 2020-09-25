class User:

	# This is an example of a class variable
	active_users = 0

	# class method
	# cls means the class if you print it you will see the class User
	# This method returns how many users there are
	@classmethod
	def display_active_users(cls):
		return f"There are {User.active_users} active users."

	# another example of a class method
	# here we are taking in a string and manufacturing and object of this class from data in that string
	# the last line of this method will run the __init__ method
	@classmethod
	def from_string(cls, data_string):
		first, last, age = data_string.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		# This is how you increase it
		User.active_users += 1

	def __repr__(self):
		return f"{self.first} is {self.age} years old."

	def logout(self):
		print(f"{self.first} left the chat room.")
		User.active_users -= 1

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}."

	def is_senior(self):
		return self.age > 65

	def birthday(self):
		print("Happy birthday {}!".format(self.first))
		self.age += 1
		return self.age


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# calling a class method
print(User.display_active_users())

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# calling a class method
print(User.display_active_users())

# Using the other class method

str_1 = "Joe, Smith, 39"
user3 = User.from_string(str_1)
print(user3.first, user3.last, user3.age)

# using the __repr__ method to get a better print
print(user3)
