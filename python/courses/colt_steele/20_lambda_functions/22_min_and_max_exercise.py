# def extremes(iter_in):

# 	# create a list
# 	ret_list = []

# 	ret_list.append(min(iter_in))
# 	ret_list.append(max(iter_in))

# 	return tuple(ret_list)

# x = extremes([1,2,3,4])

# print(x)

# The solution is very simple

def extremes(iter_in):

	return (min(iter_in), max(iter_in))

x = extremes([1,2,3,4])

print(x)