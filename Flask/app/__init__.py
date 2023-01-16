from flask import Flask, render_template, flash, redirect, url_for
from app import forms
from app.models import db
from flask_migrate import Migrate

from datetime import datetime
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.forms import RegestrationForm
from app.models import User

app = Flask(__name__)
app.config["SECRET_KEY"] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)


"""Таблиці для БД"""



# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}'.format(self.body)


"""Декоратори для відображення сторінок та їх вмісту"""
@app.before_first_request
def create_tables():
    db.create_all()
@login.user_loader
def load_user(id):
    return User.querry.get(int(id))


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title='Home')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
       return redirect(url_for("index"))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Incorrect login data: check password or username")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    
    return render_template("login.html", title="Sign in", form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegestrationForm()
    if form.validate_on_submit():
        flash("Congrats!")
        return redirect(url_for('login'))
    user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
    db.session.add(user)
    db.session.commit()
    return render_template('register.html', title='Register', form=form)
