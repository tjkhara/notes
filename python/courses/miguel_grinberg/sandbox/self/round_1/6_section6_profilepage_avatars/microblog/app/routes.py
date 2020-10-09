from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User

@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_seen = datetime.utcnow()
		db.session.commit()

@app.route('/')
@app.route('/index')
@login_required
def index():
	posts = [
		{
			'author':{'username' : 'John'},
			'body' : 'Beautiful day in Portland'
		},
		{
			'author':{'username' : 'TJ'},
			'body' : 'Great day in Chandigarh'
		}
	]
	return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
	# security feature - if user is currently logged in, send them back to index
	if current_user.is_authenticated: # if the use is logged in, then they cannot go to login
		return redirect(url_for('index'))
	# create instance of LoginForm
	form = LoginForm()
	# if this is a form submit and a valid one
	if form.validate_on_submit():
		# find the user in the database using the username provided
		user = User.query.filter_by(username=form.username.data).first()
		# if the user is not in the db or the password is wrong then redirect to login
		if user is None or not user.check_password(form.password.data):
			flash("Invalid username or password")
			return redirect(url_for('login'))
		# if we get here then the username is valid and password is valid
		login_user(user, remember=form.remember_me.data) # This stores the user object in the session
		# This code checks to see if the user was trying to visit some other page and was sent to the login
		# instead
		next_page = request.args.get('next') # if there is a next page get it
		# if no next page, then set this to index
		# second part checks to see that this is in the same domain
		if not next_page or url_parse(next_page).netloc != '': 
			next_page = url_for('index')
		# the user is logged in now go to index
		return redirect(next_page) # otherwise go to that next page after login
	# for GET request - just display the form
	return render_template('login.html', title='Sign In', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash("Congratulations you are now a registered user.")
		return redirect(url_for('login'))
	return render_template('register.html', title="Register", form=form)

@app.route('/user/<username>')
@login_required
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	posts = [
		{'author' : user, 'body' : 'Test post #1'},
		{'author' : user, 'body' : 'Test post #2'},
	]
	return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=["GET", "POST"])
@login_required
def edit_profile():
	form = EditProfileForm()

	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash("Your changes have been saved.")
		return redirect(url_for('edit_profile'))
	# prepopulating the form with database info
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title='Edit Profile', form=form)
