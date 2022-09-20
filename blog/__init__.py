import logging.config

from flask import Flask

from .models import init_app as models_init_app
from .auth import init_app as auth_init_app


def create_app(configfile=None):
    app = Flask(__name__, instance_relative_config=True)
    configfile = configfile if configfile else 'config.py'
    app.config.from_pyfile(configfile)
    # 初始化日志
    logging.config.dictConfig(app.config['LOGGING'])
    for init in [
        models_init_app,
        auth_init_app
    ]:
        init(app)
    return app