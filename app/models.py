from flask_login import  UserMixin, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db




class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(120))
    
    def __repr__(self) -> str:
        return f'<User {self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Good(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    body = db.Column(db.String(512))
    price = db.Column(db.Integer)
    

    def __repr__(self) -> str: 
        return f'<Name {self.name}'