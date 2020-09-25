# set comprehension

set_1 = {x**2 for x in range(0,10)}

print(set_1)

# dict comprehension

dict_1 = {x:x**2 for x in range(0,10)}

print(dict_1)

# another example of set comprehension

set_2 = {char.upper() for char in 'hello'}

print(set_2)

# another example

def are_all_vowels_in_string(string):
	return len({char for char in string if char in 'aeiou'}) == 5

rough_1 = are_all_vowels_in_string("haeioullo")

print(rough_1)