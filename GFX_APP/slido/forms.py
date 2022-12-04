# forms.py slido


from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired


class AddSlidoForm(FlaskForm):
    event_code = StringField('Event Code')
    submit = SubmitField('Add to List')
