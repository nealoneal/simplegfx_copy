# views.py projects

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import Project
from GFX_APP.projects.forms import AddCISForm, LoadCISForm

projects_blueprint = Blueprint('projects', __name__, template_folder='templates/projects')


@projects_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddCISForm()
    if form.validate_on_submit():
        print(f'{form} validated')
        cis = form.cis.data
        project_name = form.project_name.data
        producer = form.producer.data
        new_project = Project(cis=cis, project_name=project_name, producer=producer)
        with app.app_context():
            db.session.add(new_project)
            db.session.commit()
        form.cis.data = ""
        form.project_name.data = ""
        form.producer.data = ""
        print(cis)
        session['cis'] = cis
        session['project_name'] = project_name
        session['producer'] = producer
        readout = [f"CIS-{cis}", f"{project_name }", f"PM: {producer}"]
        session['readout'] = readout
        session['key_list'] = []
        print(readout)
        return redirect(url_for('name_keys.add_key'))

    return render_template('add_project.html', form=form)

@projects_blueprint.route('/lookup', methods=['GET','POSt'])
def lookup():
    form = LoadCISForm()
    if form.validate_on_submit():
        cis = form.cis.data
        session['cis'] = cis
        project = Project.query.get(cis)
        project_name = project.project_name
        producer = project.producer
        session['project_name'] = project_name
        session['producer'] = producer
        return redirect(url_for('view_all.view_all'))
    return render_template('load_project.html', form=form)