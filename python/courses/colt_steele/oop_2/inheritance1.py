class Animal:
	def __init__(self):
		pass

	cool = True

	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	pass


blue = Cat()

print(isinstance(blue, Cat))
print(isinstance(blue, Animal))

