from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config):
    app = Flask(__name__)

    if config == 'dev':
        from config.development import Development
        config = Development
    if config == 'prod':
        from config.production import Production
        config = Production

    with app.app_context():

        app.config.from_object(config)

        from .views.admin.routes import admin_blueprint
        from .views.instructor.routes import instructor_blueprint

        app.register_blueprint(admin_blueprint)
        app.register_blueprint(instructor_blueprint)

        from .database.db import db

        db.init_app(app)
        db.create_all()

        return app