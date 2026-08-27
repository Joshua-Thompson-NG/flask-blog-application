from flask import render_template,flash,redirect,url_for

from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post

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
