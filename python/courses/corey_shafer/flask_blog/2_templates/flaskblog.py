from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
	{
		'author' : 'TJ Khara',
		'title' : 'Blog Post 1',
		'content' : 'First post content',
		'date_posted' : 'Sept 21st 2020'
	},
	{
		'author' : 'Miles Khara',
		'title' : 'Blog Post 2',
		'content' : 'First post content',
		'date_posted' : 'Sept 22st 2020'
	}
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == "__main__":
	app.run(debug=True)