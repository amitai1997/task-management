from app import db
import datetime
from dataclasses import dataclass
import bcrypt
from flask import Flask, current_app


@dataclass
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.first_name = first_name
        self.last_name = last_name
        self.registered_on = datetime.datetime.now()
