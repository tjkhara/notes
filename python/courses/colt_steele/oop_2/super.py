class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def make_sound(self, sound):
		print(f"this animal says {sound}")

	def __repr__(self):
		return f"{self.name} is a {self.species}"

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

# For the cat class you can also do the following if you want to hard code the species to cat

# class Cat(Animal):
# 	def __init__(self, name, breed, toy):
# 		super().__init__(name, species="cat")
# 		self.breed = breed
# 		self.toy = toy

# blue = Cat("blue", "fold", "string")

blue = Cat("blue", "cat", "fold", "string")

print(blue)

print(blue.play())











