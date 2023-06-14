from app.repositories.user_role_permission_repository import UserRolePermissionRepository


class UserRolePermissionService:
    def __init__(self):
        self.user_role_permission_repository = UserRolePermissionRepository()

    def get_all_user_role_permissions(self, data):
        return self.user_role_permission_repository.get_all_user_role_permissions(data)

    def get_user_role_permission_by_id(self, user_role_permission_id):
        return self.user_role_permission_repository.get_user_role_permission_by_id(user_role_permission_id)

    def create_user_role_permission(self, data):
        return self.user_role_permission_repository.create_user_role_permission(data)

    def update_user_role_permission(self, user_role_permission_id, data):
        return self.user_role_permission_repository.update_user_role_permission(user_role_permission_id, data)

    def delete_user_role_permission(self, user_role_permission_id):
        return self.user_role_permission_repository.delete_user_role_permission(user_role_permission_id)
