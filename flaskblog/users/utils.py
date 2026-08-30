import os,secrets
from PIL import Image
from flask import url_for
from flaskblog import mail
from flask_mail import Message
from flask import current_app as app

# Save Img func
def save_img(form_picture):
    random_hex = secrets.token_hex(8)
    _,ext = os.path.splitext(form_picture.filename)

    picture_filename = random_hex + ext
    picture_path = os.path.join(app.root_path, 'static/pics', picture_filename)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request then ignore this email and no changes will be made
    '''
    mail.send(msg)