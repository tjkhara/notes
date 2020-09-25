'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''

def compact(list_in):
	return [val for val in list_in if val]


print(compact([0,1,2,"",[], False, {}, None, "All done"]))



