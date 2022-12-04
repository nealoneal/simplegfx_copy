# forms.py urls


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired


class AddURLsForm(FlaskForm):
    url = StringField('url')
    submit = SubmitField('Add to List')
