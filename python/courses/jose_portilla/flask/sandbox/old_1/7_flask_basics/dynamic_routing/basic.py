from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello Puppy!</h1>"

@app.route('/information')
def info():
	return "<h1>Puppies are cute</h1>"	

# This is dynamic routing
@app.route('/puppy/<name>')
def puppy(name):
	return f"<h1>My puppy's name is {name.upper()}</h1>"	

if __name__ == "__main__":
	app.run()