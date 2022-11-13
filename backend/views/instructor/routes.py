from flask import Blueprint, render_template


instructor_blueprint = Blueprint(
    'instructor', __name__, url_prefix='/instructor', template_folder='instructor/templates')


@instructor_blueprint.route('/')
def instructor_dashboard():
    return render_template('instructor/instructor.html')
