from app import db
import datetime
from dataclasses import dataclass
import bcrypt
from flask import Flask, current_app
from .base_model import BaseModel


@dataclass
class User(BaseModel, db.Model):
    __tablename__ = "user"
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    registered_on: str

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
        self.password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt(current_app.config['BCRYPT_LOG_ROUNDS']))
        self.first_name = first_name
        self.last_name = last_name
        self.registered_on = datetime.datetime.now()

    def serialize(self) -> dict:
        serialized_model = super().serialize()
        serialized_model.pop('password', None)
        return serialized_model
