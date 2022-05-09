from flask import Blueprint, render_template, request
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

@auth.route('/signup')
def signup():
    return render_template('profile.html')

@auth.route('/logout')
def logout():
    return 'Logout'