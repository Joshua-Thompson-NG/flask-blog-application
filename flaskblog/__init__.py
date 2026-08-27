import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Load environment variables from .env file
load_dotenv()

# --- Flask Setup/Configuration ---
app = Flask(__name__) # flask instance

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',"dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # db instance
bcrypt = Bcrypt(app)  # bcrypt instance


login_manager = LoginManager(app) # login manager instance
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes