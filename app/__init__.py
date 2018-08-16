# app/__init__.py

from flask import Flask

# local import
from instance.config import app_config

# Load the views

from app import views

def create_app(config_name):
    from app import views
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app





#added
# Initialize the app
#app = Flask(__name__, instance_relative_config=True)



# Load the config file
#instance.config.from_object('config')



#removed from def
#app = FlaskAPI(__name__, instance_relative_config=True)