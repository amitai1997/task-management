from flask import jsonify, request, Blueprint
from datetime import datetime
from app import authenticator


class BaseAPI(Blueprint):
    def __init__(self, name, import_name, url_prefix, service):
        self.service = service
        super().__init__(name, import_name, url_prefix=url_prefix)
        self.add_url_rules()

    def add_custom_url_rule(self, rule, endpoint=None, view_func=None, **options):
        self.add_url_rule(rule, endpoint=endpoint,
                          view_func=view_func, **options)

    def add_url_rules(self):
        self.add_url_rule('/', methods=['GET'],
                          view_func=self.get_all_instances)
        self.add_url_rule(
            '/<int:id>', methods=['GET'], view_func=self.get_instance)
        self.add_url_rule('/', methods=['POST'],
                          view_func=self.create_instance)
        self.add_url_rule(
            '/<int:id>', methods=['PUT'], view_func=self.update_instance)
        self.add_url_rule(
            '/<int:id>', methods=['DELETE'], view_func=self.delete_instance)

    def get_all_instances(self):
        filter_params = self._parse_filter_params()
        sort_params = request.args.get('sort_by')
        limit = request.args.get('limit', type=int)
        offset = request.args.get('offset', type=int)
        instances = self.service.get_all(
            filter_params, sort_params, limit, offset)
        return jsonify(instances)

    def get_instance(self, id):
        instance = self.service.get_by_id(id)
        if instance:
            return jsonify(instance)
        else:
            return jsonify({'error': f'Instance with id {id} not found'}), 404

    def create_instance(self):
        data = request.get_json()
        instance = self.service.create(**data)
        return jsonify(instance), 201

    def update_instance(self, id):
        data = request.get_json()
        instance = self.service.get_basic_by_id(id)
        if instance:
            instance = self.service.update(instance, **data)
            return jsonify(instance)
        else:
            return jsonify({'error': f'Instance with id {id} not found'}), 404

    @authenticator.requires_permission(['delete:data'])
    def delete_instance(self, id):
        instance = self.service.get_by_id(id)
        if instance:
            self.service.delete(instance)
            return jsonify({'message': 'Instance deleted'})
        else:
            return jsonify({'error': f'Instance with id {id} not found'}), 404

    def _parse_filter_params(self):
        filter_params = {}
        dt_format = "%Y-%m-%dT%H-%M-%SZ"
        if 'filter' in request.args:
            filter_expr = request.args.get('filter')
            # Assuming filter expression is in the format: (field=operator:value,field=operator:value)
            conditions = filter_expr.strip('()').split(',')
            for condition in conditions:
                field, operator, value = condition.split('=')[0], condition.split(
                    '=')[1].split(':')[0], condition.split('=')[1].split(':')[1]

                if self._is_valid_datetime(value, dt_format):
                    value = datetime.strptime(value, dt_format)
                filter_params.setdefault(field, {})[operator] = value

        return filter_params

    def _is_valid_datetime(self, string, format):
        try:
            datetime.strptime(string, format)
            return True
        except ValueError:
            return False
