# views.py slido

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import Slido
from GFX_APP.slido.forms import AddSlidoForm

slido_blueprint = Blueprint('slido', __name__, template_folder='templates/slido')


@slido_blueprint.route('/add_slido', methods=['GET','POST'])
def add_slido():
    form = AddSlidoForm()
    cis = session['cis']
    slidos = Slido.query.filter_by(cis_id=cis).all()
    print(slidos)
    if form.validate_on_submit():
        event_code = form.event_code.data
        form.event_code.data = ""
        new_locator = Slido(cis_id=cis, event_code=event_code)
        with app.app_context():
            db.session.add(new_locator)
            db.session.commit()
        slidos = Slido.query.filter_by(cis_id=cis).all()
        try:
            return render_template('add_slido.html', form=form, slidos=slidos)
        except:
            return render_template('add_slido.html', form=form)

    try:
        return render_template('add_slido.html', form=form, slidos=slidos)
    except:
        return render_template('add_slido.html', form=form)

