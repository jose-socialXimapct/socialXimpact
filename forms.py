from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired

class TwitterForm(FlaskForm):
  data = FileField(validators=[FileRequired()])
  submit = SubmitField('Submit')