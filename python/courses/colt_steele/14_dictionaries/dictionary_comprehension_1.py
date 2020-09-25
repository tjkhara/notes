# syntax
# {__:__for__in__}

# example 1

# numbers = dict(first=1, second=2, third=3)

# squared_numbers = {key:value ** 2 for key,value in numbers.items()}

# print(squared_numbers)

# example 2

# x = {num:num**2 for num in [1,2,3,4,5]}

# print(x)

# example 3

# str1 = "ABC"
# str2 = "123"

# combo = {str1[i]:str2[i] for i in range(0, len(str1))}

# print(combo)

# example 4

num_list = [1,2,3,4]

x = {num:("even" if num % 2 == 0 else "odd") for num in num_list}

print(x)