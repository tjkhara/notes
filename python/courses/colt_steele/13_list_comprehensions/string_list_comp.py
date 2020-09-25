# example 1

string_1 = "colt"

string_2 = [c.upper() for c in string_1]

print(string_2)

# example 2

friends = ['ashley', 'matt', 'michael']

friends_upper = [friend[0].upper() + friend[1:] for friend in friends]

print(friends_upper)