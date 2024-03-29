from app import db
from app.utils.helpers import serialize_model
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from .base_model import BaseModel


@dataclass
class Task(db.Model, BaseModel):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    due_date = db.Column(db.Date)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'statuses.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    status = db.relationship('Status', backref=db.backref(
        'task', cascade='all, delete-orphan'))
    project = db.relationship('Project', backref=db.backref(
        'task', cascade='all, delete-orphan'))

    def serialize(self) -> dict:
        serialized_model = super().serialize()
        serialized_model['status'] = self.status.title if self.status else None
        serialized_model['project'] = self.project.title if self.title else None
        serialized_model.pop('status_id', None)
        serialized_model.pop('project_id', None)
        return serialized_model
