from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length

class LoginForm(FlaskForm):
    username = StringField(label='用户名', validators=[Length(min=4, max=20, message='用户名长度在4-20之间')])
    password = PasswordField(label='密码', validators=[Length(min=6, max=20, message='密码长度在6-20之间')])
    submit = SubmitField(label='登录')