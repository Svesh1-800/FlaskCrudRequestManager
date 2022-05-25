from flask import render_template, url_for, request,redirect, flash
from flask import Blueprint
from database import db
from .models import Data
from .forms import UserRequestForm
from flask_login import login_required, current_user
table = Blueprint('table', __name__,template_folder='templates',static_folder='static',static_url_path='/project/static')

@table.route('/')
@login_required
def index():
    all_data = Data.query.all()
    form = UserRequestForm()
    return render_template("project/index.html", all_data = all_data, form=form, current_user= current_user )
@table.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash("New request was created")
        return redirect(url_for('table.index'))

@table.route('/update', methods = ['POST'])
@login_required
def update():
 
    if request.method == 'POST':
        
        my_data = Data.query.get(request.form.get('id'))
        
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Request was updated successfully")
 
        return redirect(url_for('table.index'))

@table.route('/delete/<id>/', methods = ['GET', 'POST'])
@login_required
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Request was deleted successfully")
 
    return redirect(url_for('table.index'))