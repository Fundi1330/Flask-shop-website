from flask import Flask, render_template, flash, redirect, request, url_for
from app.models import db
from flask_migrate import Migrate

# from datetime import datetime
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from app.forms import RegestrationForm, LoginForm, AddGoodForm
from app.models import User, Food_good, Clothes_good

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
    return User.query.get(int(id))


@app.route('/')
@app.route('/index/')
def index():
    authenticated = True
    if current_user.is_authenticated:
        authenticated = False
    return render_template('index.html', title='Home', authenticated=authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
       return redirect(url_for("index"))
    form = LoginForm()
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
        user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/good/<goodname>')
@login_required
def good(goodname):
    good = Food_good.query.filter_by(name=goodname).first()
    if good:
        pass
    else:
        good = Clothes_good.query.filter_by(name=goodname).first()
    return render_template('good.html', good=good)

@app.route('/food')
@login_required
def food():
    food_list = Food_good.query.all()
    return render_template('food.html', title='Food', food_list=food_list)

@app.route('/clothes')
@login_required
def clothes():
    clothes_list = Clothes_good.query.all()
    return render_template('clothes.html', title='Clothes', clothes_list=clothes_list)

@app.route('/add_good', methods=["GET", "POST"])
def add_good():
    form = AddGoodForm()
    if form.validate_on_submit():
        flash('Good succefully added to DataBase')
        good = None
        radio = request.form['options']
        if radio == 'food':
            good = Food_good(name=form.name.data, descreption=form.descreption.data,
            price=form.price.data)
        else:
            good = Clothes_good(name=form.name.data, descreption=form.descreption.data,
            price=form.price.data, size=form.size.data, matherial=form.matherial.data)

        db.session.add(good)
        db.session.commit()
    return render_template('add_good.html', title='Add good', form=form)