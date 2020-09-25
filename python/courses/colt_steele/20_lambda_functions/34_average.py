midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


x = list(zip(students, midterms, finals))

def average(x,y):
	return (x+y)/2

# can also do
y = list(map(lambda x:average(x[1],x[2]), x))

# y = list(map(lambda x:((x[1]+x[2])/2), x))

z = dict(zip(students, y))

print("x: ")
print(x)

print("y: ")
print(y)

print("z: ")
print(z)





















########
# map reference
# nums = [1,2,3,4,5]

# This map function will call x*2 on every element of nums
# we get back a map object
# doubles = map(lambda x:x*2,nums)