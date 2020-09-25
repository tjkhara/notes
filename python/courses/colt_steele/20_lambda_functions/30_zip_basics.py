
# First example

first_zip = zip([1,2,3],[4,5,6])
# print(list(first_zip))
print(dict(first_zip))

# zip stops as soon as the shortest iterable is exhausted





# Data for second example

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

print(list(zip(students, midterms, finals)))