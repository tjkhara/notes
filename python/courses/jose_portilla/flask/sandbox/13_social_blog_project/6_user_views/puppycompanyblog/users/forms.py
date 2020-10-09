# form based imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError # validation errors
from flask_wtf.file import FileField, FileAllowed # These allows us to have the user update their photo

# user based imports
from flask_login import current_user
from puppycompanyblog.models import User

# login form
class LoginForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Log In')

# registration form
class RegistrationForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('User Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match')])
	pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
	submit = SubmitField('Register')

	# check for email and username and make sure no one has taken those
	def check_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Your email has already been registered.')

	def check_username(self, field):
	if User.query.filter_by(username=field.data).first():
		raise ValidationError('Your username has already been registered.')

# Update user form
class UpdateUserForm(FlaskForm):

	email = StringField('Email', validators=[DataRequired(), Email()])
	username = StringField('User Name', validators=[DataRequired()])
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Update')

	# check for email and username and make sure no one has taken those
	def check_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Your email has already been registered.')

	def check_username(self, field):
	if User.query.filter_by(username=field.data).first():
		raise ValidationError('Your username has already been registered.')
