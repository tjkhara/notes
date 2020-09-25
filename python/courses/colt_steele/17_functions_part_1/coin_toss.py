from random import random

def flip_coin():
	# generate random number from 0 to 1
	r = random()
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"

for x in range(10):
	print(flip_coin())