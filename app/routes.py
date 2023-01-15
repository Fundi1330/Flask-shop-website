<<<<<<< Updated upstream
# from app import forms
# from app.models import User
# from flask import Flask


# app = Flask(__name__)

=======
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_required, login_user, logout_user, UserMixin
from flask import current_app as app
>>>>>>> Stashed changes


<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes


