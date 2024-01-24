from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from app.models import db

def create_app():
    app=Flask(__name__)   #create instance of app
    app.config['SECRET_KEY']='Meenu'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'

    db.init_app(app)
    #bcrypt.init_app(app)

    with app.app_context():
        if not path.exists('Library/instance/library.db'):
            db.create_all()
            print('created database')



    app.app_context().push()

    return app