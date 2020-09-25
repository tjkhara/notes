name = "Oprah"

# on its own this string is not an iterator
# we can test this by doing next(name)

# this will return an iterator
it = iter(name)

print(next(it))
print(next(it))
print(next(it))
print(next(it))


# when we use a for loop like

for char in "Oprah":
	print(char)

# what the for loop does behind the scenes is that it takes the string "Oprah" and calles iter on it. That returns an iterator.
# next() can be called on an iterator.

# next()
# When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.