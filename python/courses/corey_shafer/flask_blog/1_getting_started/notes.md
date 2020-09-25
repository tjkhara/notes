# notes for flask blog

Run these two commands to be able to start your app from the command line:

	export FLASK_APP=flaskblog.py
	export FLASK_DEBUG=1

With this you use the

	flask run

command.

You can also use the flask shell for some debugging.

We can also run this with python:

	from flask import Flask
	app = Flask(__name__)

	@app.route('/')
	def hello_world():
	    return '<p>Hello, World!<p>'

	if __name__ == "__main__":
	app.run(debug=True)