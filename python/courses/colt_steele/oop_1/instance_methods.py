
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

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

print(user1.full_name())
print(user1.initials())
print(user1.likes("ice cream"))
print(user1.is_senior())
print(user1.birthday())