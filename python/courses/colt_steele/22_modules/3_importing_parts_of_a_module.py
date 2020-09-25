# import what you need


# This means everything
# from random import * 

from random import choice, randint

# now we can't use random we have to use the piece we imported

x = choice([1,2,3,4,5])
print(x)

y = randint(1,100)
print(y)