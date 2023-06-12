from app.repositories.user_role_repository import UserRoleRepository


class UserRoleService:
    def __init__(self):
        self.user_role_repository = UserRoleRepository()

    def get_all_user_roles(self):
        return self.user_role_repository.get_all_user_roles()

    def get_user_role_by_id(self, user_role_id):
        return self.user_role_repository.get_user_role_by_id(user_role_id)

    def create_user_role(self, data):
        return self.user_role_repository.create_user_role(data)

    def update_user_role(self, user_role_id, data):
        return self.user_role_repository.update_user_role(user_role_id, data)

    def delete_user_role(self, user_role_id):
        return self.user_role_repository.delete_user_role(user_role_id)
