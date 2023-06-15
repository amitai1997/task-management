from app import db
from dataclasses import dataclass


@dataclass
class Aaa(db.Model):
    __tablename__ = 'aaa'
    username: tuple
    email: tuple

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
