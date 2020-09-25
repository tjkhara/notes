from basic import db,Puppy

# create all tables
db.create_all()
 
sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)

# These have not been added to the database so we should see None
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

# can do this also
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)
print(frank.id)
