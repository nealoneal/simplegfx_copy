# forms.py name_keys

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField, BooleanField
from wtforms.validators import data_required, InputRequired

class AddNameKeyForm(FlaskForm):
    name = StringField('Name:', validators=[InputRequired()], render_kw=({'placeholder': "Name"}))
    title = StringField('Title', validators=[InputRequired()], render_kw=({'placeholder': "Title"}))
    company = StringField('Company', render_kw=({'placeholder': "Company (optional)"}))

    left_aligned = BooleanField('Left-Aligned', default='checked')
    right_aligned = BooleanField('Right-Aligned', default='unchecked')
    otp = BooleanField('On-The-Phone', default='checked')

    submit = SubmitField('Add to List')


