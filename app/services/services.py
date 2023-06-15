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
