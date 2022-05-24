from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from .models import User
from flask_login import login_user, login_required, logout_user
from .forms import UserSignUpForm
auth = Blueprint('auth', __name__,template_folder='templates',static_folder='static',static_url_path='/auth/static')

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method=="GET":
        return render_template('auth/login.html')
    else:
        data = request.form
        user = User.query.filter_by(username=data['name']).first()
        if user:
            login_user(user)
            return redirect(url_for('table.index'))
        return "ЭХХХ"

@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = UserSignUpForm()
    if form.validate_on_submit():
        
        email = form.email.data
        name = form.name.data
        password = form.password.data
        check_user = User.query.filter_by(email=email).first()
        if check_user:
            
            flash("Such email is already exsist")
            return redirect(url_for('auth.signup'))
        new_user = User(username=name,email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("table.index"))
    return render_template('auth/signup.html',form= form)
 


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('table.index'))