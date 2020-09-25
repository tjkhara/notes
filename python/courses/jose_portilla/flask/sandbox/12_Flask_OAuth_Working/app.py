# before running this enter the client id and client secret
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'
os.environ['OATHLIB_RELAX_TOKEN_SCOPE'] = 'true'

################################################

from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='####',
                                  client_secret='####',
                                  offline=True,
                                  scope=["https://www.googleapis.com/auth/userinfo.email", "openid", "https://www.googleapis.com/auth/userinfo.profile"],
                                  redirect_url='/welcome')


app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    resp = google.get('/oauth2/v3/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v3/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)


if __name__ == '__main__':
        app.run()
