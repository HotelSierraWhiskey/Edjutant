from flask import Blueprint


admin_blueprint = Blueprint(
    'admin', __name__, url_prefix='/admin', template_folder='templates')


@admin_blueprint.route('/')
def admin_dashboard():
    return "<h1>Admin</h1>"
