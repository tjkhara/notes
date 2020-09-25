class GrumpyDict(dict):
	def __repr__(self):
		print ("None of your business")
		return super().__repr__()

	def __missing__(self, key):
		print(f"You want {key} well it aint here")

	def __setitem__(self, key, value):
		print("You want to change the dictionary?")
		print("Okay fine...")
		super().__setitem__(key, value)

	def __contains__(self, item):
		return super().__contains__(item)

data = GrumpyDict({"First":"Tom", "Animal":"Cat"})
print(data)
print(data['city'])

data['city'] = "Tokyo"

print('telephone' in data)