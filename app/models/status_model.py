from app import db
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class Status(db.Model, BaseModel):
    __tablename__ = 'statuses'
    id: int
    title: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title
