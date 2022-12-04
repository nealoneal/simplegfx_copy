# forms.py bugs

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired

class SelectBugsForm(FlaskForm):
    q_a = BooleanField("Q & A", default='unchecked')
    chat = BooleanField("Chat", default='unchecked')
    poll = BooleanField("Poll", default='unchecked')
    survey = BooleanField("Survey", default='unchecked')
    raise_hand = BooleanField('Raise Your Hand', default='unchecked')
    submit = SubmitField('Add to List', default='unchecked')