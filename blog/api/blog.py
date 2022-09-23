from os import abort
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity

from blog.models import BlogOrm, BlogModel, db, UserOrm
from blog.respbody import BlogResponse, StatusResponse, Code
from blog.log import get_logger

class BlogResource(Resource):
    def __init__(self) -> None:
        self.logger = get_logger(BlogResource.__name__)

    @jwt_required(True)
    def get(self, blog_id=None):
        identity = get_jwt_identity()
        self.logger.debug(identity)
        if blog_id:
            blog = BlogOrm.query.filter(BlogOrm.id==blog_id).all()
        else:
            blog = BlogOrm.query.all()
        blogs = [BlogModel.from_orm(b) for b in blog]
        if identity:
            user: UserOrm = UserOrm.query.filter(UserOrm.username==identity).first()
        for blog in blogs:
            blog.author_name = UserOrm.query.filter(UserOrm.id==blog.author_id).first().username
            blog.editable = True if identity and user.id == blog.author_id else False
        resp = BlogResponse(blogs=blogs).dict()
        self.logger.debug(resp)
        return resp

    @jwt_required()
    def post(self, blog_id=None):
        title = request.json['title']
        body = request.json['body']
        self.logger.debug(f'post title: {title}')
        try:
            db.session.add(BlogOrm(author_id=current_user.id, title=title, body=body))
            db.session.commit()
        except Exception as e:
            return StatusResponse(code=Code.FAIL, message=e).dict()
        else:
            return StatusResponse().dict()

    # @jwt_required(True)
    def put(self, blog_id=None):
        content = request.json
        self.logger.debug(content)
        if 'like' in content:
            try:
                BlogOrm.query.filter(BlogOrm.id==blog_id).update({BlogOrm.like: BlogOrm.like + 1})
                db.session.commit()
            except Exception as e:
                return StatusResponse(code=Code.FAIL, message=e).dict()
        return StatusResponse().dict()
        