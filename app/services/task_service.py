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
        return self.task_repo.create_task(data)

    def update_task(self, task_id, data):
        return self.task_repo.update_task(task_id, data)

    def delete_task(self, task_id):
        return self.task_repo.delete_task(task_id)
