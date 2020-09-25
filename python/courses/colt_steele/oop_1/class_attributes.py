class User:

	# This is an example of a class variable
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		# This is how you increase it
		User.active_users += 1

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



# This is how you print the value of a class variable
print(User.active_users)

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# This is how you print the value of a class variable
print(User.active_users)

user1.logout()

# This is how you print the value of a class variable
print(User.active_users)