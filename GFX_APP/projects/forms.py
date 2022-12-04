# forms.py projects
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired

class AddCISForm(FlaskForm):
    cis = IntegerField('CIS', validators=[InputRequired()], render_kw=({'placeholder': "CIS (Number Only)"}))
    project_name = StringField('Project Name', render_kw=({'placeholder': "Project Name"}))
    producer = StringField('Producer', render_kw=({'placeholder': "Producer"}))

    submit = SubmitField('Save Info')

class LoadCISForm(FlaskForm):
    cis = IntegerField('CIS', validators=[InputRequired()], render_kw=({'placeholder': "CIS (Number Only)"}))
    submit = SubmitField('Lookup Project')
