midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# we want to make something like this
# final_grades = {'dan':98, 'ang':91, 'kate':78}

# how to do this using dict comprehension
score_zip = list(zip(finals, midterms))

max_score_list = [max(x) for x in score_zip]

dict_name_score = dict(zip(students, max_score_list))

print(score_zip)

print(max_score_list)

print(dict_name_score)





# ref for list comp

# nums = [1,2,3]

# example 1

# list_1 = [x*10 for x in nums]










# reference for dict comprehension

# syntax
# {__:__for__in__}

# example 1

# numbers = dict(first=1, second=2, third=3)

# squared_numbers = {key:value ** 2 for key,value in numbers.items()}

# print(squared_numbers)

######

