from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from app import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    

class RegestrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Use a different username')

    def validate_username(self, username):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Use a different email')

class UserForm(FlaskForm):
    real_name = StringField('Real Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')