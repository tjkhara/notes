from flask import Flask

app = Flask(__name__)

# import the blueprints
from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages

# register blueprints
app.register_blueprint(core)
app.register_blueprint(error_pages)