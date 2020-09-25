midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# we want to make something like this
# final_grades = {'dan':98, 'ang':91, 'kate':78}
# final_grades = [pair for pair in zip(midterms, finals)]

# x = [max(pair) for pair in zip(midterms, finals)]

# print(final_grades)
# print(x)

# using lambda and map

# combine all into one


x = list(zip(students, midterms, finals))

y = list(map(lambda x:max(x[1],x[2]), x))

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