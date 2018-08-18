#app/__init__.py
from instance.config import app_config

def create_app(config_name):
    from .views import app
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    return app


