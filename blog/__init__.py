import logging.config

from flask import Flask, render_template
from flask_jwt_extended import jwt_required

from .models import init_app as models_init_app
from .auth import init_app as auth_init_app
from .error import init_app as error_init_app


@jwt_required(True)
def index():
    return render_template('index.html')

@jwt_required(True)
def login():
    return render_template('login.html')


def create_app(configfile=None):
    app = Flask(__name__, instance_relative_config=True)
    configfile = configfile if configfile else 'config.py'
    app.config.from_pyfile(configfile)
    logging.config.dictConfig(app.config['LOGGING'])
    for init in [
        models_init_app,
        auth_init_app,
        error_init_app,
    ]:
        init(app)
    # add index view
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/login', view_func=login)
    return app