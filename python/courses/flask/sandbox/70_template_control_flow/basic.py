from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    logged_in = False
    return render_template("basic.html", logged_in = logged_in)

if __name__ == "__main__":
    app.run(debug=True)
