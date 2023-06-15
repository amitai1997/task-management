
from flask import request, jsonify
from app.controllers.base_controller import BaseAPI
from app.services.services import *


class AaaAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/aaa"):
        super().__init__(name, import_name, url_prefix, AaaService())
        self.aaa_service = AaaService()
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


class PermissionAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/permission"):
        super().__init__(name, import_name, url_prefix, PermissionService())
        self.permission_service = PermissionService()
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


class ProjectAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/project"):
        super().__init__(name, import_name, url_prefix, ProjectService())
        self.project_service = ProjectService()
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


class StatusAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/status"):
        super().__init__(name, import_name, url_prefix, StatusService())
        self.status_service = StatusService()
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


class TaskAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/task"):
        super().__init__(name, import_name, url_prefix, TaskService())
        self.task_service = TaskService()

        def update_task_status(task_id):
            if not request.is_json:
                return jsonify({'error': 'Invalid request format'}), 400

            data = request.get_json()
            new_status = data.get('status')

            if not new_status:
                return jsonify({'error': 'Missing "status" field in request data'}), 400

            task = self.task_service.update_task_status(task_id, new_status)

            if task:
                return jsonify(task), 200
            else:
                return jsonify({'error': 'Task not found'}), 404

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
        self.add_url_rule('/<int:task_id>/status',
                          methods=['PUT'], view_func=update_task_status)
