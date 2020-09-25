from flask import Flask

app = Flask(__name__) 

@app.route('/puppy_latin/')
def puppy_latin_index():
    return "<h1>Puppy Latin index page</h1>"

@app.route('/puppy_latin/<name>')
def puppy_latin_converter(name):
    puppy_latin_name = ""
    if name[-1] != 'y':
        puppy_latin_name = name + 'y'
    else:
        puppy_latin_name = name[0:-1] + "iful"
    return "<h1>This is a page for converting strings into puppy latin {} becomes {}</h1>".format(name, puppy_latin_name)

if __name__ == "__main__":
    app.run(debug=True)