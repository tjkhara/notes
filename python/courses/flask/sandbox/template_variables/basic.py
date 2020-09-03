from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "Jose"
    name_list = list(name)
    return render_template("basic.html", name=name, name_list=name_list)

if __name__ == "__main__":
    app.run(debug=True)
