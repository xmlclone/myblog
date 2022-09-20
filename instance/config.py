import os
import logging


BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'instance')


# ============================== basic config ==============================
SECRET_KEY = 'dev'
API_VERSION = '/api/v1'


# ============================== DB ==============================
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "blog.db")}'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False


# ============================== log ==============================
LOGGING = {
    'version': 1,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s %(name)s: %(message)s',
        },
        'file': {
            'format': '%(asctime)s %(levelname)s %(name)s %(filename)s(%(lineno)d): %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': logging.DEBUG,
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'filename': os.path.join(BASE_DIR, 'blog.log'),
            'when': 'D',
            'backupCount': 10,
            'level': logging.DEBUG,
        },
        'sqlalchemy_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'filename': os.path.join(BASE_DIR, 'sqlalchemy.log'),
            'when': 'D',
            'backupCount': 10,
            'level': logging.INFO,
        },
        'werkzeug_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'file',
            'filename': os.path.join(BASE_DIR, 'werkzeug.log'),
            'when': 'D',
            'backupCount': 10,
            'level': logging.INFO,
        }
    },
    'loggers': {
        'sqlalchemy': {
            'level': logging.INFO,
            'propagate': False,
            'handlers': ['sqlalchemy_file']
        },
        'werkzeug': {
            'level': logging.INFO,
            'propagate': False,
            'handlers': ['console', 'werkzeug_file']
        }
    },
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console', 'file']
    },
}