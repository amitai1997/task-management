from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.task_repo = TaskRepository()

    def get_all_tasks(self):
        return self.task_repo.get_all_tasks()

    def get_tasks_by_project(self, project_id):
        return self.task_repo.get_tasks_by_project(project_id)

    def get_task_by_id(self, task_id):
        return self.task_repo.get_task_by_id(task_id)

    def create_task(self, data):
        data['status_id'] = 1
        return self.task_repo.create_task(data)

    def update_task(self, task_id, data):
        return self.task_repo.update_task(task_id, data)

    def update_task_status(self, task_id, new_status_id):
        from app.models.task_model import Task
        from app.repositories.status_repository import StatusRepository

        task = Task.query.get(task_id)
        if task:
            status = StatusRepository().get_status_by_id(new_status_id)
            if not status:
                raise ValueError("Invalid status value")
            else:
                if task.status_id == 1 and new_status_id == 3:
                    raise ValueError(
                        'cant change a "not started" task to "finished')
                if new_status_id == 1:
                    raise ValueError(
                        'cant change a task to "not started status after started')

        data = {"status_id": new_status_id}
        task = self.task_repo.update_task(task_id, data)
        return task.serialize()

    def delete_task(self, task_id):
        return self.task_repo.delete_task(task_id)
