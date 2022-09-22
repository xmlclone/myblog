from os import abort
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user

from blog.models import BlogOrm, BlogModel, db, UserOrm
from blog.respbody import BlogResponse, StatusResponse, Code
from blog.log import get_logger

class BlogResource(Resource):
    def __init__(self) -> None:
        self.logger = get_logger(BlogResource.__name__)

    def get(self, blog_id=None):
        if blog_id:
            blog = BlogOrm.query.filter(BlogOrm.id==blog_id).all()
        else:
            blog = BlogOrm.query.all()
        self.logger.debug(blog)
        blogs = [BlogModel.from_orm(b) for b in blog]
        for blog in blogs:
            blog.author_name = UserOrm.query.filter(UserOrm.id==blog.id).first().username
        resp = BlogResponse(blogs=blogs).dict()
        self.logger.debug(resp)
        return resp

    @jwt_required()
    def post(self):
        title = request.json['title']
        body = request.json['body']
        try:
            db.session.add(BlogOrm(author_id=current_user.id, title=title, body=body))
            db.session.commit()
        except Exception as e:
            return StatusResponse(code=Code.FAIL, message=e).dict()
        else:
            return StatusResponse().dict()
        