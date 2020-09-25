numbers = [1,2,3,4,5]

# using a loop

doubled_numbers = []

for num in numbers:
	doubled_numbers.append(2 * num)

print(doubled_numbers)

# using a list comp

list_2 = [2*x for x in numbers]
print(list_2)