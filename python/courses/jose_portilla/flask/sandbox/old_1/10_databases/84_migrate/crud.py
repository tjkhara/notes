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

# select by id
puppy_one = Puppy.query.get(3)
print(puppy_one.name)

# filters
# this will produce sql code for us
puppy_frankie = Puppy.query.filter_by(name="Frankie")
# this will print a list of puppies where the name is frakie
print(puppy_frankie.all())

# update
# first grab data
first_puppy = Puppy.query.get(3)
# set age to 10
first_puppy.age = 10
# add this
db.session.add(first_puppy)
# commit it
db.session.commit()

# delete
second_puppy = Puppy.query.get(4)
db.session.delete(second_puppy)
db.session.commit()

# print all puppies
all_puppies = Puppy.query.all()
print(all_puppies)