
from flask import Flask, Blueprint

from .response import TokenResponse


bp = Blueprint('auth', __name__)


def init_app(app: Flask):
    app.register_blueprint(bp, url_prefix=f'{app.config["API_VERSION"]}/auth')


@bp.route('/get_token')
def get_token():
    return TokenResponse(token='123').json()