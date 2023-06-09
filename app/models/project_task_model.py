from app import db


class ProjectTask(db.Model):
    __tablename__ = 'project_tasks'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    project = db.relationship('Project', backref=db.backref(
        'project_tasks', cascade='all, delete-orphan'))
    task = db.relationship('Task', backref=db.backref(
        'project_tasks', cascade='all, delete-orphan'))

    def __init__(self, project_id, task_id):
        self.project_id = project_id
        self.task_id = task_id
