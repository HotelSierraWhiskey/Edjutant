from flask import Blueprint, render_template


global_blueprint = Blueprint(
    'global', __name__, url_prefix='/', template_folder='templates')


@global_blueprint.route('/register')
def register():
    return render_template('register.html')


@global_blueprint.route('/login')
def login():
    return render_template('login.html')