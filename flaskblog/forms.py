from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


# Registration Form
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired(),])

    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

    # Validation template
    # def validate_field(self,field):
    #     if field.data == '':
    #         raise ValidationError('This field is required.')

    # Validation Checks
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('The username is already taken. Please choose a different one.')

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('The email is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
