# Working with built in modules

# Modules help keep python files small

# A module is just a python file

import random

for y in range(10):
	print(random.choice(["apple","strawberry","banana"]))


# random.shuffle changes the list
x = [1,2,3,4,5]
random.shuffle(x)

print(x)