class Person():

	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height

	def __len__(self):
		return self.height



p1 = Person("TJ",36,150)

print(len(p1))