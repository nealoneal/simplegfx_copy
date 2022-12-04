from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import NameKey
from GFX_APP.name_keys.forms import AddNameKeyForm

name_keys_blueprint = Blueprint('name_keys', __name__, template_folder='templates/name_keys')


@name_keys_blueprint.route('/add_key', methods=['GET','POST'])
def add_key():
    form = AddNameKeyForm()
    cis_id = session['cis']
    try:
        name_key_rows = NameKey.query.filter_by(cis_id=cis_id).all()
        print(name_key_rows)
    except Exception as e:
        print(e)
    if form.validate_on_submit():
        # print(cis)
        name = form.name.data
        title = form.title.data
        company = form.company.data
        left_aligned = form.left_aligned.data
        right_aligned = form.right_aligned.data
        otp = form.otp.data
        # print(name)
        form.name.data = ""
        form.title.data = ""
        form.company.data = ""

        new_name_key = NameKey(cis_id=cis_id, name=name, title=title, company=company, left_aligned=left_aligned
                               , right_aligned=right_aligned, otp=otp)
        with app.app_context():
            db.session.add(new_name_key)
            db.session.commit()
        name_key_rows = NameKey.query.filter_by(cis_id=cis_id).all()
        try:
            return render_template('add_key.html', form=form, name_key_rows=name_key_rows)
        except:
            return render_template('add_key.html', form=form)
    try:
        return render_template('add_key.html', form=form, name_key_rows=name_key_rows)
    except:
        return render_template('add_key.html', form=form)

