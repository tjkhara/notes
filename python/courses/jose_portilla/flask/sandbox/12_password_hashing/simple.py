from flask_bcrypt import Bcrypt

# create hashing object
bcrypt = Bcrypt()

password = "supersecretpassword"

hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password)

# user logging in
# check if their password matches hash

check = bcrypt.check_password_hash(hashed_password, 'wrongpassword')

print(check)

check = bcrypt.check_password_hash(hashed_password, 'supersecretpassword')

print(check)