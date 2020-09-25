names = ['Lassie', 'Colt', 'Rusty']

# Return a new list with the string "Your instructor is" + each value in the array, but only if the value is less than 5 characters

# map example for reference
# doubles = map(lambda x:x*2,nums)

# filter reference
# evens = list(filter(lambda x: x % 2 == 0, l))

# first let's filter out the names that are less than 5 characters into a new list
less_than_5 = list(filter(lambda x: len(x) < 5, names))

print(less_than_5)

# now using map let's make this a list of strings

str_list = list(map(lambda x: f"Your instructor is {x}", less_than_5))

print(str_list)

# You can also write this all out in one line like this

str_list_one_line = list(map(lambda x: f"Your instructor is {x}", filter(lambda x: len(x) < 5, names)))

print(str_list_one_line)