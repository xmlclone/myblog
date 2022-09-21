import click

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Text, DateTime


db = SQLAlchemy()


@click.command('init-db', help='Initialize DB.')
def init_db():
    db.drop_all()
    db.create_all()
    click.echo('DB initialization completed.')

def init_app(app: Flask):
    db.init_app(app)
    app.cli.add_command(init_db)


class UserOrm(db.Model):
    __tablename__ = 'blog_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), unique=True, nullable=False)
    password = Column(String(20), nullable=False)

    def __str__(self):
        return self.username

class BlogOrm(db.Model):
    __tablename__ = 'blog_blog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, nullable=False)
    title = Column(String(20), nullable=False)
    body = Column(Text)
    created = Column(DateTime, default=datetime.utcnow)
    like = Column(Integer, default=0)
    star = Column(Integer, default=0)
