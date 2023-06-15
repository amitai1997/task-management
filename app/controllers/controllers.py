
from app.controllers.base_controller import BaseAPI
from app.services.services import *


class AaaAPI(BaseAPI):
    def __init__(self, name, import_name, url_prefix="/aaa"):
        super().__init__(name, import_name, url_prefix, AaaService())
        self.aaa_service = AaaService()
        self.add_url_rule('/', methods=['GET'],
                          view_func=self.get_all_instances)
        self.add_url_rule(
            '/<int:aaa>', methods=['GET'], view_func=self.get_instance)
        self.add_url_rule('/', methods=['POST'],
                          view_func=self.create_instance)
        self.add_url_rule(
            '/<int:aaa_id>', methods=['PUT'], view_func=self.update_instance)
        self.add_url_rule(
            '/<int:aaa_id>', methods=['DELETE'], view_func=self.delete_instance)


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
