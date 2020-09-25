def max_magnitude(list_nums):
	abs_list = list(map(lambda x:abs(x), list_nums))
	return max(abs_list)


print(max_magnitude([-10,1,2,3,-20]))

## alternative solution
# def max_magnitude(list_nums):
	# return max(abs(num) for num in nums)


# map example

# nums = [1,2,3,4,5]

# This map function will call x*2 on every element of nums
# we get back a map object
# doubles = map(lambda x:x*2,nums)