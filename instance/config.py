import os
import logging
import datetime


BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'instance')


# ============================== basic config ==============================
SECRET_KEY = 'dev'
API_URL = 'http://127.0.0.1:5000'
API_VERSION = '/api/v1'
API_TOKEN = '/token'

# ============================== DB ==============================
SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "blog.db")}'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False


# ============================== wtf ==============================
# wtf插件配置，不配置默认使用SECRET_KEY
WTF_CSRF_SECRET_KEY = SECRET_KEY


# ============================== jwt ==============================
# jwt插件配置，不配置默认使用SECRET_KEY
JWT_SECRET_KEY = SECRET_KEY
# token携带的位置，默认是headers
JWT_TOKEN_LOCATION = ["headers"]
# 过期时间
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)


# ============================== log ==============================
LOGGING = {
    'version': 1,
    'formatters': {
        'console': {
            # 'format': '%(asctime)s %(levelname)s %(name)s : %(message)s',
            'format': '%(asctime)s %(levelname)s %(name)s %(filename)s(%(lineno)d): %(message)s',
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
        },
        'blog': {
            'level': logging.DEBUG,
            'propagate': False,
            'handlers': ['console', 'file']
        }
    },
    'root': {
        'level': logging.DEBUG,
        'handlers': ['console', 'file']
    },
}