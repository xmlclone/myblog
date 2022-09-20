import logging.config

from flask import Flask


def create_app(configfile=None):
    app = Flask(__name__, instance_relative_config=True)
    configfile = configfile if configfile else 'config.py'
    app.config.from_pyfile(configfile)
    # 初始化日志
    logging.config.dictConfig(app.config['LOGGING'])
    # 初始化orm
    from .models import init_app as models_init_app
    models_init_app(app)
    return app