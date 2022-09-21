from flask import Flask

from .index import IndexView
from .auth import LoginView, RegisterView

def init_app(app: Flask):
    app.add_url_rule('/', view_func=IndexView.as_view('index'))
    app.add_url_rule('/login', view_func=LoginView.as_view('login'))
    app.add_url_rule('/register', view_func=RegisterView.as_view('register'))