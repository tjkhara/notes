from puppycompanyblog import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

# This is the function that allows us to check if the user is authenticated or not
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)


class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	profile_image = db.Column(db.String(64), nullable=False, default="default_profile.png")
	email = db.Column(db.String(64), unique=True, index=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	# one to many relationship
	# one user can have many blog posts
	posts = db.relationship('BlogPost', backref='author', lazy=True)

	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f"Username {self.username}"

# This has a relationship with the User
class BlogPost(db.Model):
	
	# This is used in the ForeignKey lines below
	users = db.relationship(User)

	id = db.Column(db.Integer, primary_key=True)
	# This is what connects the user to the blog post
	# one to many - one user can have many blog posts
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	title = db.Column(db.String(140), nullable=False)
	text = db.Column(db.Text, nullable=False)

	def __init__(self, title, text, user_id):
		self.title = title
		self.text = text
		self.user_id = user_id

	def __repr__(self):
		return f"Post id {self.id} -- Date: {self.date} -- Title: {self.title}"