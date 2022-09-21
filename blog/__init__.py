import logging.config

from flask import Flask

from .models import init_app as models_init_app
from .api import init_app as api_init_app
from .error import init_app as error_init_app
from .view import init_app as view_init_app


def create_app(configfile=None):
    app = Flask(__name__, instance_relative_config=True)
    configfile = configfile if configfile else 'config.py'
    app.config.from_pyfile(configfile)
    logging.config.dictConfig(app.config['LOGGING'])
    for init in [
        models_init_app,
        api_init_app,
        error_init_app,
        view_init_app,
    ]:
        init(app)
    return app