

numbers = [1,2,3,4,5,6]

# without else
y = [num for num in numbers if num % 2 == 0]

# print(y)

# with else
x = [num*2 if num % 2 == 0 else num/2 for num in numbers]

# print(x)

# combine this with in

with_vowels = "This is too much fun!"

z = ''.join(char for char in with_vowels if char not in "aeiou")

print(z)

