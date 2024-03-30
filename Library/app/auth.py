from flask import Blueprint, render_template, flash
from flask import request, redirect, url_for
from app.models import User, Admin, db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/register_user', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
       email=request.form.get('email') 
       fname=request.form.get('fname') 
       lname=request.form.get('lname') 
       mobile_no=request.form.get('mobile_no') 
       password1=request.form.get('password1') 
       password2=request.form.get('password2') 

       reader = User.query.filter_by(user_email = email).first()
       if reader:
           flash("Account already exists, please login", category='error')
           return redirect("user_home.html")
       elif password1!=password2:
           flash('Password must be the same.', category = 'error')
       else:
           new_reader=User(user_email=email, user_fname=fname, user_lname=lname, user_mobile=mobile_no, user_password=password1)
           db.session.add(new_reader)
           db.session.commit()
           flash('Account created, please login', category = 'success')
           return redirect('/user_home')
       
    return render_template("register_user.html")


