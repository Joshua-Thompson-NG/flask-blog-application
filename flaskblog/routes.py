from flask import render_template,flash,redirect,url_for,request

from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User,Post
from flask_login import login_user,logout_user,login_required,current_user


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hashing password
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created, you can now log in",'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated: # Authentication
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):

            login_user(user,remember=form.remember.data) # login in user
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else  redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Please check email and password', 'error')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html',title='Account')