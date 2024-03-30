from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
from app.models import db, User

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

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'   
    login_manager.init_app(app)    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app