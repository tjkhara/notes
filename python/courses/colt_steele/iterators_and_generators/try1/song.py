'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num, beverage):
	for num in range(num, -1, -1):
		if num > 1:
			yield f"{num} bottles of {beverage} on the wall."
		elif num == 1:
			yield f"Only 1 bottle of {beverage} left!"
		else:
			yield f"No more {beverage} left!"

kombucha_song = make_song(5, "kombucha")
print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration
