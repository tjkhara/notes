'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''

def frequency(list_in, term):
    freq = 0
    for x in list_in:
    	if x == term:
    		freq += 1
    return freq

print(frequency([True, False, True, True], False))