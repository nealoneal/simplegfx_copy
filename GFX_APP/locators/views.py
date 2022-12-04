# views.py locators

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import Locators
from GFX_APP.locators.forms import AddLocatorForm

locators_blueprint = Blueprint('locators', __name__, template_folder='templates/locators')


@locators_blueprint.route('/add_locator', methods=['GET','POST'])
def add_locator():
    form = AddLocatorForm()
    cis = session['cis']
    locators = Locators.query.filter_by(cis_id=cis).all()
    print(locators)
    if form.validate_on_submit():
        text = form.text.data
        form.text.data = ""
        new_locator = Locators(cis_id=cis, text=text)
        with app.app_context():
            db.session.add(new_locator)
            db.session.commit()
        locators = Locators.query.filter_by(cis_id=cis).all()
        try:
            return render_template('add_locator.html', form=form, locators=locators)
        except:
            return render_template('add_locator.html', form=form)

    try:
        return render_template('add_locator.html', form=form, locators=locators)
    except:
        return render_template('add_locator.html', form=form)

