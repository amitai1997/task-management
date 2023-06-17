from flask import request, jsonify
from app.controllers.base_controller import BaseAPI
from app.services.services import *


class AaaAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/aaa"):
        super().__init__(name, import_name, url_prefix, AaaService())


class PermissionAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/permission"):
        super().__init__(name, import_name, url_prefix, PermissionService())


class ProjectAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/project"):
        super().__init__(name, import_name, url_prefix, ProjectService())


class StatusAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/status"):
        super().__init__(name, import_name, url_prefix, StatusService())


class TaskAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/task"):
        super().__init__(name, import_name, url_prefix, TaskService())

        self.add_custom_url_rule(
            '/<int:task_id>/status', methods=['PUT'], view_func=self.update_task_status)

    def update_task_status(self, task_id):
        if not request.is_json:
            return jsonify({'error': 'Invalid request format'}), 400

        data = request.get_json()
        new_status = data.get('status')

        if not new_status:
            return jsonify({'error': 'Missing "status" field in request data'}), 400

        task = self.service.update_task_status(task_id, new_status)

        if task:
            return jsonify(task), 200
        else:
            return jsonify({'error': 'Task not found'}), 404


class UserAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/user"):
        super().__init__(name, import_name, url_prefix, UserService())


class UserRoleAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/user-role"):
        super().__init__(name, import_name, url_prefix, UserRoleService())


class UserRolePermissionAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/user-role-permission"):
        super().__init__(name, import_name, url_prefix, UserRolePermissionService())
