from flask import redirect, render_template, url_for, Blueprint
from flask import Flask
from GFX_APP import db, app

# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)