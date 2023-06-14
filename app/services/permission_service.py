from app.repositories.permission_repository import PermissionRepository


class PermissionService:
    def __init__(self):
        self.permission_repo = PermissionRepository()

    def get_all_permissions(self, data):
        return self.permission_repo.get_all_permissions(data)

    def get_permission_by_id(self, permission_id):
        return self.permission_repo.get_permission_by_id(permission_id)

    def create_permission(self, data):
        return self.permission_repo.create_permission(data)

    def update_permission(self, permission_id, data):
        return self.permission_repo.update_permission(permission_id, data)

    def delete_permission(self, permission_id):
        return self.permission_repo.delete_permission(permission_id)
