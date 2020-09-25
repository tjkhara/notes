list_1 = [1,2,3]
list_2 = [3,4,5]
list_3 = [6,7,8]

list_4 = [list_1, list_2, list_3]

# print(list_4)

# iterating through items in nested lists

# for l in list_4:
# 	for item in l:
# 		print(item)

# nested list comprehension

# x = [[print(val) for val in l] for l in list_4]

y = [[print(item) for item in l] for l in list_4]

print(y)