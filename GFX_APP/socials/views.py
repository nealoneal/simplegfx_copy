# views.py socials

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import Socials
from GFX_APP.socials.forms import AddSocialForm

socials_blueprint = Blueprint('socials', __name__, template_folder='templates/socials')


@socials_blueprint.route('/add_social', methods=['GET','POST'])
def add_social():
    form = AddSocialForm()
    cis = session['cis']
    socials = Socials.query.filter_by(cis_id=cis).all()
    print(socials)
    if form.validate_on_submit():
        text = form.text.data
        form.text.data = ""
        new_social = Socials(cis_id=cis, text=text)
        with app.app_context():
            db.session.add(new_social)
            db.session.commit()
        socials = Socials.query.filter_by(cis_id=cis).all()
        try:
            return render_template('add_social.html', form=form, socials=socials)
        except:
            return render_template('add_social.html', form=form)

    try:
        return render_template('add_social.html', form=form, socials=socials)
    except:
        return render_template('add_social.html', form=form)

