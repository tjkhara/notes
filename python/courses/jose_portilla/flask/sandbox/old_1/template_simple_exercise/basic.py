from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')


@app.route('/thank_you')
def thank_you():
    username = request.args.get('username')
    error_messages = []

    # if username is empty
    if username == "":
        error_messages.append("Username cannot be empty")
        return render_template('username_error.html', username=username, error_messages=error_messages)


    # Check if the username contains a lowercase letter
    contains_lower_case_letter = False

    import string

    # lower case letter check
    contains_lower_case_letter = False

    lower_case_letters = string.ascii_lowercase
    for c in username:
        if c in lower_case_letters:
            contains_lower_case_letter = True
            break

    # upper case letter check
    contains_upper_case_letter = False

    upper_case_letters = string.ascii_uppercase

    for u in username:
        if u in upper_case_letters:
            contains_upper_case_letter = True
            break

    # username must end in a number
    ends_in_number = False

    numbers_list = list(range(0, 10))

    last_char = username[-1]

    if last_char.isnumeric():
        ends_in_number = True

    # creating a list of errors
    if not contains_lower_case_letter:
        error_messages.append("Your username does not contain a lower case letter.")
    if not contains_upper_case_letter:
        error_messages.append("Your username does not contain an upper case letter.")
    if not ends_in_number:
        error_messages.append("Your username does not end in a number.")

    if contains_lower_case_letter and contains_upper_case_letter and ends_in_number:
        return render_template('thankyou.html', username=username, error_messages=error_messages)
    else:
        return render_template('username_error.html', username=username, error_messages=error_messages)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
