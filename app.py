import os

from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from forms import RegistrationForm,LoginForm

from models import User,Post

# Load environment variables from .env file
load_dotenv()

# --- Flask Setup/Configuration ---
app = Flask(__name__) # flask instance
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # db instance


# --- Dummy Data ---
posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'Blog Post 2',
        'date_posted':'July 20, 2020'
    },

    {
        'author':'John Doe',
        'title':'Blog Post 2',
        'content':'Blog Post 3',
        'date_posted':'July 21, 2020'
    },

    {
        'author':'Mike',
        'title':'Blog Post 3',
        'content':'Blog Post 4',
        'date_posted':'July 22, 2020'
    }
]

# --- Page Routes ---
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html",title="About")

@app.route('/contact')
def contact():
    return "<h1> Contact Page </h1>"


# --- Form Routes ---
@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account Created for {form.username.data}!",'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)