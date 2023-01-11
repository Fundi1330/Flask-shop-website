from flask import Flask, render_template, flash, redirect, url_for
from flask_migrate import Migrate
from app import forms
from app.models import User, db
from flask_login import current_user, login_required, login_user, logout_user, LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False

db.init_app(app) #Add this line Before migrate line
login = LoginManager(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title='Home', user=current_user)

@login.user_loader
def load_user(id):
    return User.querry.get(int(id))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Incorrect login data: check password or username")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign in", form=form)
    

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.before_first_request
def create_tables():
    db.create_all()

app.app_context().push()

# from app import routes








# @app.route('/userinfo', methods=["GET", "POST"])
# def additional_info():
#     form = forms.UserForm()
#     if form.validate_on_submit():
#         flash(f'Additional info requested for user {form.real_name.data}, phone_number={form.phone_number.data}')
#         return redirect('/')
#     return render_template('userinfo.html', title='Add Additional Info', form=form)