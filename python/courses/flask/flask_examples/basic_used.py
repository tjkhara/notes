from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

@app.route('/information')
def info():
    return "<h1>puppies are cute</h1>"

@app.route('/information2')
def info2():
    return "<h1>puppies are cute - yes another one</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name[100])

if __name__ == "__main__":
    app.run(debug=True)