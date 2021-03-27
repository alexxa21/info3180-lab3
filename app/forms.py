from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [Email(), DataRequired()])
    subject = StringField("Subject", validators = [DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])