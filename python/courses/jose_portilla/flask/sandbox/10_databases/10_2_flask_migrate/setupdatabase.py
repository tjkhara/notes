from basic import db, Puppy

# creates all the tables
# takes classes and converts them into tables
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)
miles = Puppy('Miles', 10)

# These will say none because they are not in the database yet
# They don't have any ids
print(sam.id)
print(frank.id)
print(miles.id)

# Add these two objects to the database
db.session.add_all([sam, frank, miles])

# commit changes
db.session.commit()

print(sam.id)
print(frank.id)
print(miles.id)