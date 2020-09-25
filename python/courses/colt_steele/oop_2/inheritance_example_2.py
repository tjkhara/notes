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

class Moderator(User):
	
	total_mods = 0

	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {Moderator.total_mods} active moderators."

	def remove_post(self):
		return f"{self.full_name} removed a post from the {self.community} community"


print(User.display_active_users())
u1 = User("Tom", "Garcia", 35)
u2 = User("Peter", "Mohan", 41)
u3 = User("Graham", "Gooch", 71)
print(User.display_active_users())

jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
print(jasmine.full_name())
print(jasmine.community)
print(User.display_active_users())

print(Moderator.display_active_mods())