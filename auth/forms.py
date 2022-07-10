from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserSignUpForm(FlaskForm):
    email = EmailField('email',render_kw={"placeholder": "Email"}, validators=[DataRequired(),Email()])
    name = StringField('name',render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = PasswordField('password',render_kw={"placeholder": "Password"}, validators=[DataRequired(), Length(min=8,message='Password should be at least %(min)d characters long')])

# not in use
class UserSignInForm(FlaskForm):
    email = EmailField('email',render_kw={"placeholder": "Email"}, validators=[DataRequired(),Email()])
    password = PasswordField('password',render_kw={"placeholder": "Password"}, validators=[DataRequired(), Length(min=8,message='Password should be at least %(min)d characters long')])


  