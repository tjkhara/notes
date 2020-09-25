def eat_junk(food):
	assert food in [
	"pizza",
	"ice cream",
	"candy",
	"fried butter"], "food must be a junk food!"
	print(f"NOM NOM NOM I am eating {food}")

food = input("Enter a food please: ")
print(eat_junk(food))