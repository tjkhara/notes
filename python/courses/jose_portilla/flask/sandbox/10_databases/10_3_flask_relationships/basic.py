# create entries into the db tables
from models import db, Puppy, Owner, Toy

# creating two puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

# Add puppies to the database
db.session.add_all([rufus, fido])
db.session.commit()

# check
# This returns all the puppies in the database
print(Puppy.query.all())

# grabbing just rufus from the database
# This gives us a list of items
# rufus = Puppy.query.filter_by(name='Rufus')

# To get just the first we can do
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus) # should have no owner here

# another option is .all() gives a list and then we get the first item
# rufus = Puppy.query.filter_by(name='Rufus').all()[0]

# create owner
jose = Owner('Jose', rufus.id)

# give toys to rufus
toy1 = Toy("chew toy", rufus.id)
toy2 = Toy("ball", rufus.id)

# commit these changes
# notice how flexible this method is it can take owner objects and toy objects at the same time
db.session.add_all([jose, toy1, toy2])
db.session.commit()

# grab rufus again after those additions
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(f"What toys does {rufus.name} have?")
rufus.report_toys()