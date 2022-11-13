from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import Config
from .globals.routes import global_blueprint


def create_app(config):
    app = Flask(__name__)

    with app.app_context():

        app.config.from_object(Config(config))

        from .views.admin.routes import admin_blueprint
        from .views.instructor.routes import instructor_blueprint

        app.register_blueprint(global_blueprint)
        app.register_blueprint(admin_blueprint)
        app.register_blueprint(instructor_blueprint)

        from .database.db import db

        db.init_app(app)
        db.create_all()

        return app
