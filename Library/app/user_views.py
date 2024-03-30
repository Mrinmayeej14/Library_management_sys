from flask import Blueprint, render_template
from flask import request, redirect, url_for
from app.models import User, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

user_views = Blueprint('user_views', __name__)

@user_views.route('/user_home')
def user_home():
    return render_template('user_home.html')

@user_views.route('/cart')
def user_cart():
    return render_template('cart.html')