from distutils.command.config import config
import requests

from flask import render_template, flash, redirect, url_for, current_app
from flask.views import MethodView

from blog.log import get_logger
from blog.respbody import Code

from .wtf import LoginForm


class LoginView(MethodView):
    def __init__(self) -> None:
        self.logger = get_logger(LoginView.__name__)

    def get(self):
        return render_template('login.html', form=LoginForm())

class RegisterView(MethodView):
    def get(self):
        return render_template('register.html')