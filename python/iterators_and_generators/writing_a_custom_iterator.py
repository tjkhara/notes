class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	# This method makes this iterable
	# This needs to return an iterator
	def __iter__(self):
		return self

	# define the behavior of next
	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration
		


for x in Counter(0,10):
	print(x)