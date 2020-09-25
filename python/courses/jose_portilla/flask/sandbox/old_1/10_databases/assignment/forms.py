from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddOwnerForm(FlaskForm):

    name = StringField('Name of Owner:')
    puppy_id = IntegerField('Id of puppy:')
    submit = SubmitField('Add Owner')


class AddForm(FlaskForm):

    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Puppy to Remove:')
    submit = SubmitField('Remove Puppy')