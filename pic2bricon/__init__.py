import flask

# Set up flask
app = flask.Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("config.py")
flask.Flask.instance_path = app.auto_find_instance_path()

# Import views
from pic2bricon.views import *
