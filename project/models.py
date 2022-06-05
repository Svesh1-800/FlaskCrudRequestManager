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
    #data_type_id = db.Column(db.Integer,db.ForeignKey('data-type.id')) # это на будущее

    def __init__(self,name,email,phone,user_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_id = user_id


class DataType(db.Model):
    __tablename__ = 'data-type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


    def __repr__(self):
        return '<DataType {}>'.format(self.name)

