# generator expressions are a lighter weight version of a list we can't do append etc

names = ["Cristy", "Cole", "Cameron"]

y = all(x[0] == 'C' for x in names)

print(y)