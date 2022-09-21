from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from blog.models import UserOrm
from blog.log import get_logger

from .user import UserResource, TokenResource


jwt = JWTManager()
logger = get_logger('api')


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


def init_app(app: Flask):
    api = Api(app)
    api.add_resource(UserResource, f'{app.config["API_VERSION"]}/user', endpoint='api.user')
    api.add_resource(TokenResource, f'{app.config["API_VERSION"]}/token', endpoint='api.token')
    jwt.init_app(app)