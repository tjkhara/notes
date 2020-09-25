from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello Puppy!</h1>"

@app.route('/information')
def info():
	return "<h1>Puppies are cute</h1>"	

# This is dynamic routing
@app.route('/puppy_latin/<name>')
def puppy(name):
	if name[-1] == 'y':
		new_name = "" + name[:-1] + "iful"
	else:
		new_name = name + "y"
	return f"<h1>My puppy's name is {new_name}</h1>"	

if __name__ == "__main__":
	app.run(debug=True)