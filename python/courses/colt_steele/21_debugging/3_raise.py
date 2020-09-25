def colorize(text, color):
	colors = ('cyan','yellow','blue','green')

	if type(color) is not str:
		raise TypeError("color must be a string")

	if type(text) is not str:
		raise TypeError("text must be a string")

	if color not in colors:
		raise ValueError("color is invalid color")

	print(f"printed {text} in {color}")

# This is the ideal usage
# colorize("hello", "red")

colorize("hello", "red")