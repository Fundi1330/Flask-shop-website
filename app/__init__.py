from flask import Flask, render_template, flash, redirect, url_for
from app import forms
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False


app.app_context().push()

# from app import routes
db = SQLAlchemy(app)
Migrate = Migrate(app, db)
login = LoginManager(app)


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

@app.before_first_request
def create_tables():
    db.create_all()
@login.user_loader
def load_user(id):
    return User.querry.get(int(id))
    

class Good(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    body = db.Column(db.String(512))
    price = db.Column(db.Integer)
    

    def __repr__(self) -> str: 
        return f'<Name {self.name}'


@app.route('/')
@app.route('/index/')
def index():
    
    user = db.Query
    posts = [
        {
            'author': {'username': 'Lisa', 'age': 53},
            'body': 'Stupid russia'
        },
        {
            'author': {'username': 'Ben', 'age': 18},
            'body': 'CSS is cool'
        }
    ]

    return render_template('index.html', title='Home', posts=posts)

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/userinfo', methods=["GET", "POST"])
def additional_info():
    form = forms.UserForm()
    if form.validate_on_submit():
        flash(f'Additional info requested for user {form.real_name.data}, phone_number={form.phone_number.data}')
        return redirect('/')
    return render_template('userinfo.html', title='Add Additional Info', form=form)