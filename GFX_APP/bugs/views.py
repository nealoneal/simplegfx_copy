# views.py bugs

from flask import Flask, render_template, redirect, url_for, Blueprint, session
from GFX_APP import db, app
from GFX_APP.models import DefaultBugs
from GFX_APP.bugs.forms import SelectBugsForm

bugs_blueprint = Blueprint('bugs', __name__, template_folder='templates/bugs')


@bugs_blueprint.route('/select_bugs', methods=['GET','POST'])
def select_bugs():
    form = SelectBugsForm()
    cis = session['cis']
    bugs = DefaultBugs.query.filter_by(cis_id=cis).first()
    bug_list = []
    try:
        if bugs.q_a == 1:
            bug_list.append('Q & A')
        if bugs.chat == 1:
            bug_list.append(", Chat ")
        if bugs.poll == 1:
            bug_list.append(", Poll")
        if bugs.survey == 1:
            bug_list.append(", Survey")
        if bugs.raise_hand == 1:
            bug_list.append(", Raise Hand")
    except Exception as e:
        print(e)
        pass
    if form.validate_on_submit():
        q_a = form.q_a.data
        chat = form.chat.data
        poll = form.poll.data
        survey = form.survey.data
        raise_hand = form.raise_hand.data
        form.q_a.data = ""
        form.chat.data = ""
        form.poll.data = ""
        form.survey.data = ""
        form.raise_hand.data = ""

        selected_bugs = DefaultBugs(cis_id=cis, q_a=q_a,chat=chat,poll=poll,survey=survey,raise_hand=raise_hand)
        with app.app_context():
            db.session.add(selected_bugs)
            db.session.commit()
        bugs = DefaultBugs.query.filter_by(cis_id=cis).first()
        try:
            bug_list = []
            if bugs.q_a == 1:
                bug_list.append('Q & A')
            if bugs.chat == 1:
                bug_list.append(", Chat ")
            if bugs.poll == 1:
                bug_list.append(", Poll")
            if bugs.survey == 1:
                bug_list.append(", Survey")
            if bugs.raise_hand == 1:
                bug_list.append(", Raise Hand")
        except Exception as e:
            print(e)
            pass
        try:
            return render_template('bug_select.html', form=form, bug_list=bug_list)
        except:
            return render_template('bug_select.html', form=form)

    try:
        return render_template('bug_select.html', form=form, bug_list=bug_list)
    except:
        return render_template('bug_select.html', form=form)

