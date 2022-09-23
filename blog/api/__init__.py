from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from blog.models import UserOrm
from blog.log import get_logger

from .user import UserResource, TokenResource
from .blog import BlogResource


jwt = JWTManager()
logger = get_logger('api')


@jwt.user_identity_loader
def user_identity_cb(user: UserOrm):
    logger.debug(user)
    return user.username

@jwt.user_lookup_loader
def user_lookup_cb(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = UserOrm.query.filter(UserOrm.username==identity).first()
    logger.debug(f'identity: {identity}, user: {user}')
    return user

def init_app(app: Flask):
    api = Api(app)
    api.add_resource(UserResource, f'{app.config["API_VERSION"]}/user', endpoint='api.user')
    api.add_resource(TokenResource, f'{app.config["API_VERSION"]}/token', endpoint='api.token')
    api.add_resource(BlogResource, f'{app.config["API_VERSION"]}/blog', f'{app.config["API_VERSION"]}/blog/<int:blog_id>', endpoint='api.blog')
    # add_context_processor参数默认是False，如果需要在jinja的模板里面使用current_user，必须设置此值为True
    # 但是所有通过jinja渲染的视图，必须有jwt_required修饰，不管是否需要jwt认证，都需要
    jwt.init_app(app, add_context_processor=False)