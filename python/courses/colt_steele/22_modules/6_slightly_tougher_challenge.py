from keyword import iskeyword


def contains_keyword(*args):
	l = map(lambda a:iskeyword(a), args)
	return any(l)

print(contains_keyword("fine","def"))










# map reference
# nums = [1,2,3,4,5]

# This map function will call x*2 on every element of nums
# we get back a map object
# doubles = map(lambda x:x*2,nums)