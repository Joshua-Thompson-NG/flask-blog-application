import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Load environment variables from .env file
load_dotenv()

# --- Flask Setup/Configuration ---
app = Flask(__name__) # flask instance
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',"dev-secret-key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # db instance

from flaskblog import routes