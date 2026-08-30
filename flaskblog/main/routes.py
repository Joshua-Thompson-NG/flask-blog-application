from flask import Blueprint,render_template,request,redirect,url_for,flash
from flaskblog.main.forms import ContactForm
from flaskblog.models import Post
from flaskblog.main.utils import send_contact_email


main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template("home.html",posts=posts)


@main.route('/about')
def about():
    return render_template("about.html",title="About")

@main.route('/contact', methods=['POST','GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_contact_email(form)
        flash('Your message has been sent. Thank you!','success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html',title='Contact',form=form)