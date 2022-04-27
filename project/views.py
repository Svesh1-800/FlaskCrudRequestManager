from flask import render_template, url_for, request,redirect, flash
from flask import Blueprint

from .models import Data, db

crud_requests = Blueprint('crud-requests', __name__)

@crud_requests.route('/')
def index():
    all_data = Data.query.all()
    return render_template("index.html", all_data = all_data)
@crud_requests.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()
        flash("New request was created")
        return redirect(url_for('crud-requests.index'))

@crud_requests.route('/update', methods = ['POST'])
def update():
 
    if request.method == 'POST':
        
        my_data = Data.query.get(request.form.get('id'))
        
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Request was updated successfully")
 
        return redirect(url_for('crud-requests.index'))

@crud_requests.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Request was deleted successfully")
 
    return redirect(url_for('crud-requests.index'))