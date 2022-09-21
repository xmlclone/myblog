from sqlite3 import IntegrityError
from flask import Flask, Blueprint, request, abort
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, current_user, get_jwt_identity
from sqlalchemy.exc import IntegrityError

from .respbody import TokenResponse, StatusResponse
from .reqbody import UserRequest
from .models import db, UserOrm
from .log import get_logger


bp = Blueprint('auth', __name__)
jwt = JWTManager()
logger = get_logger('auth')


def init_app(app: Flask):
    app.register_blueprint(bp, url_prefix=f'{app.config["API_VERSION"]}/auth')
    jwt.init_app(app, True)


@jwt.user_identity_loader
def user_identity_lookup(user: UserOrm):
    logger.debug(user)
    return user.username

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = UserOrm.query.filter(UserOrm.username==identity).first()
    logger.debug(f'identity: {identity}, user: {user}')
    return user


@bp.route('/register', methods=['POST'])
def register():
    req = UserRequest.parse_obj(request.json)
    try:
        db.session.add(UserOrm(username=req.username, password=req.password))
        db.session.commit()
    except IntegrityError:
        abort(404, f'Username {req.username} already exists.')
    except Exception as e:
        abort(404, e)
    else:
        return StatusResponse().json()

@bp.route('/token', methods=['POST'])
def token():
    req = UserRequest.parse_obj(request.json)
    user: UserOrm = UserOrm.query.filter(UserOrm.username == req.username).first_or_404()
    token = create_access_token(user)
    return TokenResponse(token=token).json()

@bp.route('/')
@jwt_required()
def test_jwt():
    identity = get_jwt_identity()
    logger.debug(f'identity: {identity}, current_user: {current_user}')
    return 'index'