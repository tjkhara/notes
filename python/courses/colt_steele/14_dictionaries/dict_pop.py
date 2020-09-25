d = dict(a=1,b=2,c=3)

item = d.pop('a')

print(d)
print(item) #1

# pop something that does not exist

item_1 = d.pop('z')

print(item_1) # key error