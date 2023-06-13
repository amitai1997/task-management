from app import db
from app.models.task_model import Task


class TaskRepository:
    def get_all_tasks(self, data):
        tasks = Task.query.filter_by(**data).all()
        return [task.serialize() for task in tasks]

    def get_task_by_id(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return task.serialize()
        else:
            return None

    def create_task(self, data):
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
        return task.serialize()

    def update_task(self, task_id, data):
        task = Task.query.get(task_id)
        if task:
            for key, value in data.items():
                setattr(task, key, value)
            db.session.commit()
            return task
        else:
            return None

    def delete_task(self, task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        else:
            return False
