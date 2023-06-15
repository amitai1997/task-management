from app import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, instance_id):
        instance = self.model.query.get(instance_id)
        if instance:
            return instance.serialize()
        else:
            return None

    def get_all(self, data):
        instances = self.model.query.filter_by(**data).all()
        return [instance.serialize() for instance in instances]

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance.serialize()

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance.serialize()

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()
