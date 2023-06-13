from app import db
from dataclasses import dataclass


@dataclass
class Status(db.Model):
    __tablename__ = 'statuses'
    id: int
    title: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title
