from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SelectField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email, Length


class ContactForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    region = SelectField(u'Region', choices=[('', ''),('North America', 'North America'), ('South America', 'South America'), ('Caribbean', 'Caribbean'),
                                             ('Europe', 'Europe'), ('Australia', 'Australia')])
    message = TextAreaField('Message', validators=[InputRequired()])

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired])
    password = StringField('Password', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(4, 32)])
    password = PasswordField('Password', validators=[InputRequired(), Length(8, 64)])


