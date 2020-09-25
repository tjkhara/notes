def speak(animal = "dog"):
	if animal == "dog":
		return "woof"
	if animal == "pig":
		return "oink"
	if animal == "duck":
		return "quack"
	if animal == "cat":
		return "meow"
	return "?"

print(speak())
