from flask import Flask

app = Flask(__name__)

# import the blueprint
from puppycompanyblog.core.views import core
# register blueprint
app.register_blueprint(core)