

# method 1

# d = {}.fromkeys(['a','e','i','o','u'],0)

# print(d)

# method 2

# d = {v:0 for v in ['a','e','i','o','u']}

# print(d)

# method 3

d = dict.fromkeys("aeiou",0)

print(d)