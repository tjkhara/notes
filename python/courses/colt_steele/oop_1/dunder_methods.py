class Person:
	def __init__(self):
		self.name = "Tony"
		self._secret = "hi!"


p = Person()

print(p.name, p._secret)