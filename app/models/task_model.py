from app import db
from app.utils.helpers import serialize_model


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    due_date = db.Column(db.Date)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    status = db.relationship('Status', backref=db.backref(
        'tasks', cascade='all, delete-orphan'))
    project = db.relationship('Project', backref=db.backref(
        'tasks', cascade='all, delete-orphan'))

    def serialize(self) -> dict:
        serialized_model = serialize_model(self)
        serialized_model['status'] = self.status.title if self.status else None
        serialized_model.pop('status_id', None)
        return serialized_model
