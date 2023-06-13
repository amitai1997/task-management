from app import db
from dataclasses import dataclass


@dataclass
class Task(db.Model):
    __tablename__ = 'tasks'
    id: int
    title: str
    description: str
    due_date: str
    project_id: int
    status_id: int

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    due_date = db.Column(db.Date)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'statuses.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    status = db.relationship('Status', backref=db.backref(
        'tasks', cascade='all, delete-orphan'))
    project = db.relationship('Project', backref=db.backref(
        'tasks', cascade='all, delete-orphan'))

    def __init__(self, title, description, due_date=None, status_id=None, project_id=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status_id = status_id
        self.project_id = project_id
