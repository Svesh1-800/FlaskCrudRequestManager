from database import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __repr__(self):
        return '<User {}>'.format(self.username) 
        
    def set_password(self, password):
	    self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
	    return check_password_hash(self.password_hash, password)
    