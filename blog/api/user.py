from sqlite3 import IntegrityError
from flask import request, abort
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_

from blog.respbody import TokenResponse, StatusResponse, Code
from blog.reqbody import UserRequest
from blog.models import db, UserOrm
from blog.log import get_logger


class UserResource(Resource):
    def __init__(self) -> None:
        self.logger = get_logger(UserResource.__name__)

    def post(self):
        req = UserRequest.parse_obj(request.json)
        try:
            db.session.add(UserOrm(username=req.username, password=req.password))
            db.session.commit()
        except IntegrityError:
            return StatusResponse(code=Code.CONFLICT, message=f'用户【{req.username}】已存在').dict()
        except Exception as e:
            abort(404, e)
        else:
            return StatusResponse().dict()


class TokenResource(Resource):
    def __init__(self) -> None:
        self.logger = get_logger(TokenResource.__name__)

    def get(self):
        req = UserRequest.parse_obj(request.json)
        self.logger.debug(req)
        user: UserOrm = UserOrm.query.filter(and_(UserOrm.username==req.username, UserOrm.password==req.password)).first()
        self.logger.debug(user)
        if not user:
            return StatusResponse(code=Code.AUTHFAIL, message='用户名或密码错误').dict()
        token = create_access_token(user)
        self.logger.debug(f'User: {user}, get token: {token}')
        return TokenResponse(token=token).dict()
