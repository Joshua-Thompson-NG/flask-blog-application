from flask import current_app as app
from flask_mail import Message
from flaskblog import mail


def send_contact_email(form):
    msg = Message(
        subject=f"[Flask Blog Contact] {form.subject.data}",
        recipients=[app.config['MAIL_DEFAULT_SENDER']],
        reply_to=form.email.data
    )
    msg.body = f'''You received a new message from the Contact page:

From: {form.name.data} <{form.email.data}>
Subject: {form.subject.data}

{form.message.data}
'''
    mail.send(msg)