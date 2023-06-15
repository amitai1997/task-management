from app.services.base_service import BaseService
from app.repositories.repositories import *


class AaaService(BaseService):
    def __init__(self):
        super().__init__(AaaRepository())


class PermissionService(BaseService):
    def __init__(self):
        super().__init__(PermissionRepository())


class ProjectService(BaseService):
    def __init__(self):
        super().__init__(ProjectRepository())


class StatusService(BaseService):
    def __init__(self):
        super().__init__(StatusRepository())


class TaskService(BaseService):
    def __init__(self):
        super().__init__(TaskRepository())

    def update_task_status(self, task_id, new_status_id):

        from app.models.task_model import Task
        from app.repositories.repositories import StatusRepository

        task = self.get_basic_by_id(task_id)
        if task:
            status = StatusRepository().get_by_id(new_status_id)
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
        task = self.update(task, **data)
        return task
