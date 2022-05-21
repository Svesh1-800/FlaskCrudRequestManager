from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import db
from .models import User


auth = Blueprint('auth', __name__,template_folder='templates')

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method=="GET":
        return render_template('auth/login.html')
    else:
        data = request.form
        user = User.query.get(username=data['name'])
        if user:
            return "ОН СУЩЕСТВУЕТ"
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
    return 'Logout'