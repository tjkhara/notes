'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(list_in, call_back_func):
	truthy_list = []
	falsey_list = []

	for el in list_in:
		if(call_back_func(el)):
			truthy_list.append(el)
		else:
			falsey_list.append(el)
	return [truthy_list, falsey_list]



def isEven(num):
    return num % 2 == 0

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
