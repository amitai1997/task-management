from app import db


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(20))
    # project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
