import os  # for setting base dir
# from forms import AddForm, DelForm, AddOwnerForm  # my own forms.py file and it's forms
from flask import Flask  # for the flask app and it's methods and functions
from flask_sqlalchemy import SQLAlchemy  # for accessing and working with sqlite db
from flask_migrate import Migrate  # for updating FLASK_APP

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'datah.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "cccccclcdgvkdtluuvelgjcehtguhnickhdnrckneehf"

db = SQLAlchemy(app)
Migrate(app, db, render_as_batch=True)

from GFX_APP.projects.views import projects_blueprint
app.register_blueprint(projects_blueprint, url_prefix='/projects')
from GFX_APP.name_keys.views import name_keys_blueprint
app.register_blueprint(name_keys_blueprint, url_prefix='/name_keys')
from GFX_APP.bugs.views import bugs_blueprint
app.register_blueprint(bugs_blueprint, url_prefix='/bugs')
from GFX_APP.socials.views import socials_blueprint
app.register_blueprint(socials_blueprint, url_prefix='/socials')
from GFX_APP.locators.views import locators_blueprint
app.register_blueprint(locators_blueprint, url_prefix='/locators')
from GFX_APP.slido.views import slido_blueprint
app.register_blueprint(slido_blueprint, url_prefix='/slido')
from GFX_APP.urls.views import urls_blueprint
app.register_blueprint(urls_blueprint, url_prefix='/urls')
from GFX_APP.view_all.views import view_all_blueprint
app.register_blueprint(view_all_blueprint, url_prefix='/view_all')