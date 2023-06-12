from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_all_users(self):
        return self.user_repo.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repo.get_user_by_id(user_id)

    def create_user(self, data):
        return self.user_repo.create_user(data)

    def update_user(self, user_id, data):
        return self.user_repo.update_user(user_id, data)

    def delete_user(self, user_id):
        return self.user_repo.delete_user(user_id)
