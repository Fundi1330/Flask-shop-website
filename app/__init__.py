from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import User, db
from app import routes
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False

from models import db
db.init_app(app) #Add this line Before migrate line
login = LoginManager(app)
migrate = Migrate(app, db)



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