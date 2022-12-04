# forms.py socials


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired


class AddSocialForm(FlaskForm):
    text = StringField('text')
    submit = SubmitField('Add to List')
