# Note we imported request!
from flask import Flask, render_template, request
from check import check_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This page will have the sign up form
@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

# This page will be the page after the form
@app.route('/thankyou')
def thank_you():
    username = request.args.get('username')
    result = check_input(username)
    if result:
        return render_template('thankyou.html',username=username)
    else:
        return render_template('problem.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
