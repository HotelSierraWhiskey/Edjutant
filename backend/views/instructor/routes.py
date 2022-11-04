from flask import Blueprint


instructor_blueprint = Blueprint('instructor', __name__, url_prefix='/instructor', template_folder='templates')

@instructor_blueprint.route('/')
def instructor_dashboard():
    return "<h1>Instructor</h1>"