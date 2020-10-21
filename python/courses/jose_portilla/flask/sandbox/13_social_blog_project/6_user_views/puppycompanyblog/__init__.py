import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# import the blueprints
from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.error_pages.handlers import error_pages

# register blueprints
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)

# Databse setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# Login configs
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login' # The view that users needs to go to when they login