from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), index = True, unique = True)
    email = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(120))
    admin = db.Column(db.Boolean, index = True, default=False)
    
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Clothes_good(UserMixin, db.Model):
    __tablename__ = 'Clothes_Goods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45), index = True, unique = True)
    description = db.Column(db.String(120), index = True, unique = True)
    size = db.Column(db.String(10), index = True)
    material = db.Column(db.String(75), index = True)
    
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)

class Food_good(UserMixin, db.Model):
    __tablename__ = 'Food_Goods'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), index = True, unique = True)
    description = db.Column(db.String(80), index = True, unique = True)
    price = db.Column(db.Float, index=True)
    
    def __repr__(self) -> str:
        return f'name: {self.name}, price: {self.price}'