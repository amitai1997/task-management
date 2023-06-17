class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, instance_id):
        return self.repository.get_by_id(instance_id)

    def get_basic_by_id(self, instance_id):
        return self.repository.get_basic_by_id(instance_id)

    def get_all(self, filter_params=None, sort_params=None, limit=None):
        return self.repository.get_all(filter_params=filter_params, sort_params=sort_params, limit=limit)

    def create(self, **kwargs):
        return self.repository.create(**kwargs)

    def update(self, instance, **kwargs):
        return self.repository.update(instance, **kwargs)

    def delete(self, instance):
        self.repository.delete(instance)
