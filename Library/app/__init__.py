from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
#from app.models import *
from app.models import db

def create_app():
    app=Flask(__name__)   #create instance of app
    app.config['SECRET_KEY']='Meenu'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'
    db.init_app(app)
    app.app_context().push()
    

    with app.app_context():
        if not path.exists('Library/instance/library.db'):
            db.create_all()
            print('created database')

    from .user_views import user_views
    from .auth import auth

    app.register_blueprint(user_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    

    return app