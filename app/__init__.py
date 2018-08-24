#app/__init__.py

from flask_api import FlaskAPI
import psycopg2

#local import
from instance.config import app_config

#intialize psycopg2
db = psycopg2.connect(host="localhost",database="test_db", user="postgres", password="root")
cur = db.cursor()


def create_app(config_name):
    from .views import app
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app


