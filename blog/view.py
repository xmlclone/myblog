from flask import Flask, render_template, url_for, redirect
from flask_jwt_extended import jwt_required, current_user

from .log import get_logger

logger = get_logger('view')

def init_app(app: Flask):
    @app.route('/editor')
    def editor():
        return render_template('editor.html')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/blog/add')
    @jwt_required(locations=["query_string"])
    def blog_add():
        return render_template('blogedit.html', blog_id=None, oper_type='New', current_user=current_user)

    @app.route('/blog/view/<int:blog_id>')
    def blog_view(blog_id: int):
        logger.debug(f'view blog id: {blog_id}')
        return render_template('blogview.html', blog_id=blog_id)

    @app.route('/blog/update/<int:blog_id>')
    @jwt_required(locations=["query_string"])
    def blog_edit(blog_id: int=1):
        logger.debug(f'edit blog id: {blog_id}')
        return render_template('blogedit.html', blog_id=blog_id, oper_type='Update', current_user=current_user)
        # 编辑暂时不可用，先跳转到首页
        return redirect('/')

    # 发现编辑blog的场景下，edit.md自动加载其lib会在url前面增加blog，先重定向到static目录
    @app.route('/blog/static/<path:subpath>')
    def subpath_replace(subpath):
        logger.debug(subpath)
        return redirect(f'/static/{subpath}')