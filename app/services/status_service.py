from app.repositories.status_repository import StatusRepository


class StatusService:
    def __init__(self):
        self.status_repo = StatusRepository()

    def get_all_statuses(self):
        return self.status_repo.get_all_statuses()

    def get_status_by_id(self, status_id):
        return self.status_repo.get_status_by_id(status_id)

    def create_status(self, data):
        return self.status_repo.create_status(data)

    def update_status(self, status_id, data):
        return self.status_repo.update_status(status_id, data)

    def delete_status(self, status_id):
        return self.status_repo.delete_status(status_id)
