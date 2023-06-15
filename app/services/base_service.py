class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self, data):
        return self.repository.get_all(data)

    def get_by_id(self, obj_id):
        return self.repository.get_by_id(obj_id)

    def create(self, **data):
        return self.repository.create(**data)

    def update(self, obj_id, **data):
        return self.repository.update(obj_id, **data)

    def delete(self, obj_id):
        return self.repository.delete(obj_id)
