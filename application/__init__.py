from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# secret key generated using python3 CLI interpreter
# used to protect the application against cross-site scripting (also knows as XSS) and cookie modificcation
# >> import secrets
# >> secrets.token_hex(32)
app.config['SECRET_KEY'] = 'e41ea80c121d9f8778579e53a29e31865739d4cf749b0cb1f04e2c629743a80f'

# sqlite settings using SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database instatiation
db = SQLAlchemy(app)

# bcrypt object that holds the keys
pwcrypt = Bcrypt(app)

# login manager instantiation
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.setup_app(app)

from application import site

# app.config['WTF_CSRF_ENABLED'] = True
