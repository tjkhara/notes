'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(list_in):
    name_list = []
    for d in list_in:
    	name_list.append(d['first'] + " " + d['last'])
    return name_list

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

extract_full_name(names)