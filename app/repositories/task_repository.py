from app import db
from app.models.task_model import Task


class TaskRepository:
    def get_all_tasks(self):
        tasks = Task.query.all()
        return [task for task in tasks]

    def get_tasks_by_project(self, project_id):
        tasks = Task.query.filter_by(project_id=project_id).all()
        return [task for task in tasks]

    def get_task_by_id(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return task
        else:
            return None

    def create_task(self, data):
        task = Task(**data)
        db.session.add(task)
        db.session.commit()
        return task

    def update_task(self, task_id, data):
        task = Task.query.get(task_id)
        if task:
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.due_date = data.get('due_date', task.due_date)
            task.status = data.get('status', task.status)
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
