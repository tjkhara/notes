# generator function to create an iterator
def week():
	days = [
	"Monday", 
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday"
	]

	for day in days:
		yield day


# use the generator to create an iterator
week = week()

# iterate through the iterator
for day in week:
	print(day)