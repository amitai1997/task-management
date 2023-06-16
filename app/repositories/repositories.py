from app.repositories.base_repository import BaseRepository
from app.models.aaa_model import Aaa
from app.models.permission_model import Permission
from app.models.project_model import Project
from app.models.status_model import Status
from app.models.task_model import Task
from app.models.user_model import User
from app.models.user_roles_model import UserRole
from app.models.user_role_permission_model import UserRolePermission


class AaaRepository(BaseRepository):
    def __init__(self):
        super().__init__(Aaa)


class PermissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(Permission)


class ProjectRepository(BaseRepository):
    def __init__(self):
        super().__init__(Project)


class StatusRepository(BaseRepository):
    def __init__(self):
        super().__init__(Status)


class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(Task)


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)


class UserRoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserRole)


class UserRolePermissionRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserRolePermission)
