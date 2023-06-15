from app import db
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class Project(db.Model, BaseModel):
    __tablename__ = 'projects'
    id: int
    title: str
    description: str

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(256))

    def __init__(self, title, description):
        self.title = title
        self.description = description
