'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list_in):
	if len(list_in) == 0:
		return None
	else:
		return list_in[-1]

		
    