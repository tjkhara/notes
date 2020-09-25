'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list_in, command, location, value=None):
    if command == "remove" and location == "end":
    	return list_in.pop()
    if command == "remove" and location == "beginning":
    	return list_in.pop(0)
    if command == "add" and location == "beginning":
    	list_in.insert(0, value)
    	return list_in
    if command == "add" and location == "end":
    	list_in.append(value)
    	return list_in


l1 = [1,2,3,4,5]

# x = list_manipulation(l1, "remove", "beginning")
# print(x)

# y = list_manipulation(l1, "remove", "end")
# print(y)

# y = list_manipulation(l1, "add", "beginning", 10)
# print(y)

y = list_manipulation(l1, "add", "end", 10)
print(y)