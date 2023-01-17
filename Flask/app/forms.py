from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User
from flask import flash


"""Форми на сайті"""
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember ME')
    submit = SubmitField('Sign In')


class RegestrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign In')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Use a different username')

    def validate_username(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            flash('Use a different email')


class AddGoodForm(FlaskForm):
    name = StringField('Good name', validators=[DataRequired()])
    descreption = StringField('Good descreption', validators=[DataRequired()])
    price = StringField('Good price', validators=[DataRequired()])
    size = StringField('Size')
    matherial = StringField('Matherial')
    submit = SubmitField('Add good')
