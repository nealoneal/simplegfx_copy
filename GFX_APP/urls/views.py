# views.py urls

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import URLs
from GFX_APP.urls.forms import AddURLsForm

urls_blueprint = Blueprint('urls', __name__, template_folder='templates/urls')


@urls_blueprint.route('/add_url', methods=['GET','POST'])
def add_url():
    form = AddURLsForm()
    cis = session['cis']
    urls = URLs.query.filter_by(cis_id=cis).all()
    print(urls)
    if form.validate_on_submit():
        url = form.url.data
        form.url.data = ""
        new_url = URLs(cis_id=cis, url=url)
        with app.app_context():
            db.session.add(new_url)
            db.session.commit()
        urls = URLs.query.filter_by(cis_id=cis).all()
        try:
            return render_template('add_url.html', form=form, urls=urls)
        except:
            return render_template('add_url.html', form=form)

    try:
        return render_template('add_url.html', form=form, urls=urls)
    except:
        return render_template('add_url.html', form=form)

