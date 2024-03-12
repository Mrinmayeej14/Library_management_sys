from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
#from . import db

from flask_login import UserMixin

db=SQLAlchemy()
bcrypt=Bcrypt()

class User(db.Model, UserMixin):
    __tablename__="user"
    user_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email=db.Column(db.String(45), unique=True, nullable=False)
    user_password=db.Column(db.String(45), nullable=False)
    user_fname = db.Column(db.String(45), nullable=False)
    user_lname = db.Column(db.String(45))
    user_mobile = db.Column(db.String(10), nullable=False, unique=True)
    user_address = db.Column(db.Text)
    cart = db.Column(db.Text, nullable=False, default = '{}')
    orders = db.Column(db.Text, default = '{}')

    def get_id(self):
        return int(self.user_id)

class Admin(db.Model, UserMixin):
    __tablename__= "admin"
    admin_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_email = db.Column(db.String(45), unique=True, nullable=False)
    admin_password = db.Column(db.String(45), nullable=False)
    admin_fname = db.Column(db.String(45), nullable=False)
    admin_lname = db.Column(db.String(45))
    admin_mobile = db.Column(db.String(10), nullable=False)

    def get_id(self):
        return int(self.admin_id) 
    
class Book(db.Model):
    __tablename__= "book"
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(45), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'), nullable=False)
    price = db.Column(db.Integer, nullable = False)
    publishing_date = db.Column(db.Date)
    book_img = db.Column(db.String, nullable=False)
    book_issue_date = db.Column(db.Date)
    book_return_date = db.Column(db.Date)
    total_sold = db.Column(db.Integer, default = 0)

    def get_id(self):
        return int(self.product_id)
    
class Genre(db.Model):
    __tablename__= "genre"
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_name = db.Column(db.String(45), nullable=False, unique=True)
    books = db.relationship('Book', backref = 'genre')
    genre_img = db.Column(db.String, nullable=False)

    def get_id(self):
        return int(self.category_id)