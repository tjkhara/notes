from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'tkhara'}
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
	return render_template('index.html', title='Home', user=user, posts=posts)