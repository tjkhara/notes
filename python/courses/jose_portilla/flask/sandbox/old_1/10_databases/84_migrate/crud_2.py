from basic import db,Puppy

## create
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
# this command saves it
db.session.commit()

## read
# return list of puppy objects in the table
all_puppies = Puppy.query.all()
print(all_puppies)