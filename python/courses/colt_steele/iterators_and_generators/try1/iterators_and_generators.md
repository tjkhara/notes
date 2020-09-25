# Iterators and generators

## Iterators

an object that can be iterated upon. And object which returns data, one element at a time when next() is called on it.

## Iterable

An object that will return an iterator when iter() is called on it.

### Examples:

"HELLO" is an iterable but not an iterator.

iter("HELLO") returns an iterator.

## Next function

When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error.