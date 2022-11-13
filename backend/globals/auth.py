from database.db import db
from werkzeug.security import generate_password_hash, check_password_hash


def register_user(registration):
    username = registration['username']
    password_hash = generate_password_hash(registration['password'])
    db.session.execute(f"INSERT INTO trial.users(username, password) VALUES('{username}', '{password_hash}')")
    db.session.commit()

