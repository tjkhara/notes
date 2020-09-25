

first = dict(a=1,b=2,c=3,d=4,e=5)
second = {}

# this makes second like first
second.update(first)

# print(second)

# let's overwrite an existing key
second['a'] = "AMAZING"

# print(second)

# let's update again
second.update(first)
# becomes the same as first again
print(second)