from flask import jsonify, request, Blueprint


class BaseAPI(Blueprint):
    def __init__(self, name, import_name, url_prefix, service):
        self.service = service
        super().__init__(name, import_name, url_prefix=url_prefix)

    def get_all_instances(self):
        data = {}
        if request.is_json:
            data = request.get_json()
        instance = self.service.get_all(data)
        return jsonify(instance)

    def get_instance(self, id):
        instance = self.service.get_by_id(id)
        if instance:
            return jsonify(instance)
        else:
            return jsonify({'error': 'Instance not found'}), 404

    def create_instance(self):
        data = request.get_json()
        instance = self.service.create(**data)
        return jsonify(instance), 201

    def update_instance(self, id):
        data = request.get_json()
        instance = self.service.get_by_id(id)
        if instance:
            instance = self.service.update(instance, **data)
            return jsonify(instance)
        else:
            return jsonify({'error': 'Instance not found'}), 404

    def delete_instance(self, id):
        instance = self.service.get_by_id(id)
        if instance:
            self.service.delete(instance)
            return jsonify({'message': 'Instance deleted'})
        else:
            return jsonify({'error': 'Instance not found'}), 404