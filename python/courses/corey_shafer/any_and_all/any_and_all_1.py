numbers1 = [2,4,6,8,10]

numbers2 = [1,2,3,4,5,6]

evens1 = []

for num in numbers1:
	evens1.append(num % 2 == 0)

print(evens1)

# The all function returns true is all values are true
# seems like the all function is like an AND operator
# and any will probably be like the OR operator

result = all(evens1)

print(result)


another_list = [False, False, False]

print(any(another_list))