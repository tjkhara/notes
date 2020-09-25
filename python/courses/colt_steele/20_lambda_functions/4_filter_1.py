l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

print(evens)


##################
# Example 2
##################

names = ['amit', 'peter', 'ashutosh', 'ajai']

a_names = list(filter(lambda x : x[0] == 'a', names))

print(a_names)