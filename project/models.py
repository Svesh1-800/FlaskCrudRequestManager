import datetime
from database import db
from werkzeug.security import generate_password_hash,  check_password_hash
from auth.models import User
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    data_type = db.Column(db.String(100))
    #data_type_id = db.Column(db.Integer,db.ForeignKey('data-type.id')) # это на будущее
    #department_id = db.Column(db.Integer,db.ForeignKey('data-type.id')) # это на будущее

    def __init__(self,name,email,phone,req_type,user_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.data_type = req_type
        self.user_id = user_id

# not in use
class DataType(db.Model):
    __tablename__ = 'data-type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


    def __repr__(self):
        return '<DataType {}>'.format(self.name)
    
#not in use
class Department(db.Model):
    __tablename__='department'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(300))
    active = db.Column(db.Boolean,default=True)

    def __repr__(self):
        return '<Department {}>'.format(self.name)

    def __str__(self):
        return 'Department: {}'.format(self.name)

