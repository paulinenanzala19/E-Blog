from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    username = StringField('Enter your username',validators = [InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')