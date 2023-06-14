from app import db
from app.models.permission_model import Permission


class PermissionRepository:
    def get_all_permissions(self, data):
        permissions = Permission.query.filter_by(**data).all()
        return [permission for permission in permissions]

    def get_permission_by_id(self, permission_id):
        permission = Permission.query.get(permission_id)
        if permission:
            return permission
        else:
            return None

    def create_permission(self, data):
        permission = Permission(**data)
        db.session.add(permission)
        db.session.commit()
        return permission

    def update_permission(self, permission_id, data):
        permission = Permission.query.get(permission_id)
        if permission:
            for key, value in data.items():
                setattr(permission, key, value)
            db.session.commit()
            return permission
        else:
            return None

    def delete_permission(self, permission_id):
        permission = Permission.query.get(permission_id)
        if permission:
            db.session.delete(permission)
            db.session.commit()
            return True
        else:
            return False
