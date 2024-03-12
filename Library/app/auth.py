from flask import Blueprint, render_template
from flask import request, redirect, url_for
from app.models import User, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET'])

def home():
    return render_template("user_home.html")