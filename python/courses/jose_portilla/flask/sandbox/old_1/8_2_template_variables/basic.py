from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    some_variable = "Jose"
    # pass in a list to html
    some_list = [1,2,3,4]
    # pass in a dict
    some_dict = {"name":"TJ", "fun":"sometimes"}
    return render_template('basic.html', some_variable=some_variable, some_list=some_list, some_dict=some_dict)

if __name__ == '__main__':
    app.run(debug=True)
