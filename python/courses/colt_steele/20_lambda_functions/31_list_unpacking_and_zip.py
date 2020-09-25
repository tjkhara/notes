# list unpacking to send in arguments one by one

five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]

print(list(zip(*five_by_two)))