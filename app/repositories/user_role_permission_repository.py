from app import db
from app.models.user_role_permission_model import UserRolePermission


class UserRolePermissionRepository:
    def get_all_user_role_permissions(self, data):
        user_role_permissions = UserRolePermission.query.filter_by(
            **data).all()
        return [user_role_permission for user_role_permission in user_role_permissions]

    def get_user_role_permission_by_id(self, user_role_permission_id):
        user_role_permission = UserRolePermission.query.get(
            user_role_permission_id)
        if user_role_permission:
            return user_role_permission.serialize()
        else:
            return None

    def create_user_role_permission(self, data):
        user_role_permission = UserRolePermission(**data)
        db.session.add(user_role_permission)
        db.session.commit()
        return user_role_permission

    def update_user_role_permission(self, user_role_permission_id, data):
        user_role_permission = UserRolePermission.query.get(
            user_role_permission_id)
        if user_role_permission:
            for key, value in data.items():
                setattr(user_role_permission, key, value)
            db.session.commit()
            return user_role_permission
        else:
            return None

    def delete_user_role_permission(self, user_role_permission_id):
        user_role_permission = UserRolePermission.query.get(
            user_role_permission_id)
        if user_role_permission:
            db.session.delete(user_role_permission)
            db.session.commit()
            return True
        else:
            return False
