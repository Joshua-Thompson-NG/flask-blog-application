import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# Load environment variables from .env file
load_dotenv()

# --- Flask Setup/Configuration ---
app = Flask(__name__) # flask instance

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',"dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # db instance
bcrypt = Bcrypt(app)  # bcrypt instance

# --- Mail Setup ---
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail = Mail(app)


login_manager = LoginManager(app) # login manager instance
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)