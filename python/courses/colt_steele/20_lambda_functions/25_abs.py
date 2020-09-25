# absolute value
print(abs(-3.444))

# fabs - have to import it with math
import math

# converts to a float before taking absolute value
print(math.fabs(4))

###

# sum
# takes an iterable, takes an optional start and adds elements together
# goes from left to right
# start by default is 0

l1 = [1,2,3]

print(sum(l1)) # 6

print(sum(l1, 10)) # 16

# for floating point values with extended precision
print(math.fsum([1.0,2.0,2.222222222222222222222222]))