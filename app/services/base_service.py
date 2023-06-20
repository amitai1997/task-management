class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, instance_id):
        instance = self.repository.get_by_id(instance_id)
        return instance.serialize() if instance else None

    def get_basic_by_id(self, instance_id):
        instance = self.repository.get_basic_by_id(instance_id)
        return instance if instance else None

    def get_all(self, filter_params=None, sort_params=None, limit=None, offset=None):
        instances = self.repository.get_all(
            filter_params=filter_params, sort_params=sort_params, limit=limit, offset=offset)
        if instances:
            return [instance.serialize() for instance in instances]
        else:
            return None

    def create(self, **kwargs):
        instance = self.repository.create(**kwargs)
        return instance.serialize() if instance else None

    def update(self, instance, **kwargs):
        instance = self.repository.update(instance, **kwargs)
        return instance.serialize() if instance else None

    def delete(self, instance):
        self.repository.delete(instance)
