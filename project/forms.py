from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, SelectField
from wtforms.validators import DataRequired, Email


class UserRequestForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(),Email()])
    phone = IntegerField('phone', validators=[DataRequired()])
    req_type = SelectField(
        choices = [('Meeting', 'meeting'), ('Request', 'request')],
        validators=[DataRequired()]
    )