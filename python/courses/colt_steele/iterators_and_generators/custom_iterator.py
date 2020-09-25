# this like our own range class

class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	# this method needs to return an iterator
	def __iter__(self):
		return self

	# we also have to define next
	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration





for n in Counter(50,55):
	print(n)