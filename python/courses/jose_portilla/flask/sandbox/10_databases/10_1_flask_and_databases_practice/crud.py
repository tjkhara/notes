from basic import db, Puppy

########## create
my_puppy = Puppy('Rufus', 10)
db.session.add(my_puppy)
db.session.commit()

my_puppy = Puppy('Gogo', 1)
db.session.add(my_puppy)
db.session.commit()

########## read
# This returns a list of the puppy objects in the table
all_puppies = Puppy.query.all()
print(all_puppies)

# select by id
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

puppy_three = Puppy.query.get(3)
print(puppy_three.name)

# Filters
puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam.all())
print('\n')

# produce some sql code for us
puppy_age_one = Puppy.query.filter_by(age=10)
# this prints out the list of all the puppies where the name is Frankie
print(puppy_age_one.all())

########## update
# first grab the data
first_puppy = Puppy.query.get(1)
# edit the attribute you want
first_puppy.age = 10
# update it
db.session.add(first_puppy)
# commit it
db.session.commit()

########## delete
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()


########## print out
all_puppies = Puppy.query.all()
print(all_puppies)