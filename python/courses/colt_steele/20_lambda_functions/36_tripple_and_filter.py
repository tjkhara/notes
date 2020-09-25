'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''

def triple_and_filter(num_list):
    not_div = list(filter(lambda x: x % 4 == 0, num_list))
    trippled = list(map(lambda x:3*x, not_div))
    return trippled



print(triple_and_filter([6,8,10,12]))



# map reference
# list(map(lambda x:x-1, num_list))


# for reference filter example
# evens = list(filter(lambda x: x % 2 == 0, l))