from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from .models import User
from flask_login import login_user, login_required, logout_user

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
    if request.method=="GET":
        return render_template('auth/signup.html')
    else:
        data = request.form
        email = data['email']
        name = data['name']
        password = data['password']
        check_user = User.query.filter_by(email=email).first()
        if check_user:
            flash("Такой чел уже есть")
            return redirect(url_for('auth.signup'))
        new_user = User(username=name,email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
            

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('table.index'))