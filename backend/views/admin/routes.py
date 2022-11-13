from flask import Blueprint, render_template
import os

admin_blueprint = Blueprint(
    'admin', __name__, url_prefix='/admin', template_folder='templates')


@admin_blueprint.route('/')
def admin_dashboard():
    return render_template('admin/admin.html')
