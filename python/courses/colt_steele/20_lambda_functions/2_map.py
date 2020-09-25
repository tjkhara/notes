# a map is a function that accepts at least two arguments
# 1) a function to call
# 2) an iterable
# It runs the lambda for each value in the iterable and returns a map object which can be converted
# into another data structure

nums = [1,2,3,4,5]

# This map function will call x*2 on every element of nums
# we get back a map object
doubles = map(lambda x:x*2,nums)

# we can iterate over this map object
# for num in doubles:
	# print(num)

#################
###### map objects can only be iterated once
#################

# we can convert this map object to a list as well
l1 = list(doubles)

for val in l1:
	print(val)

# Typically you would convert it into a list right away
doubles = list(map(lambda x:x*2,nums))

###################################################################
# Example 2
###################################################################

people = ["tj", "miles", "bhakti"]

# Want to make a new list with all elements upper cased
people_u = list(map(lambda x:x.upper(), people))

print(people_u)

###################################################################
# Example 3
###################################################################

names = [

	{"first":"TJ", "last":"Khara"},
	{"first":"Miles", "last":"Khara"}
]

first_names = list(map(lambda d:d["first"], names))

print(first_names)

###################################################################
# Example 4
# We can also use a normal function with map
# Dont have to use a double
################################################################

def double(x): return x**2

l2 = [1,2,3,4,5]

l3 = list(map(double, nums))

print(l3)