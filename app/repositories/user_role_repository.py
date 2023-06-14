from app import db
from app.models.user_roles_model import UserRole


class UserRoleRepository:
    def get_all_user_roles(self):
        user_roles = UserRole.query.all()
        return [user_role for user_role in user_roles]

    def get_user_role_by_id(self, user_role_id):
        user_role = UserRole.query.get(user_role_id)
        if user_role:
            return user_role
        else:
            return None

    def create_user_role(self, data):
        user_role = UserRole(
            name=data['name'],
            description=data['description']
        )
        db.session.add(user_role)
        db.session.commit()
        return user_role

    def update_user_role(self, user_role_id, data):
        user_role = UserRole.query.get(user_role_id)
        if user_role:
            user_role.name = data.get('name', user_role.name)
            user_role.description = data.get(
                'description', user_role.description)
            user_role.permissions = data.get(
                'permissions', user_role.permissions)
            db.session.commit()
            return user_role
        else:
            return None

    def delete_user_role(self, user_role_id):
        user_role = UserRole.query.get(user_role_id)
        if user_role:
            db.session.delete(user_role)
            db.session.commit()
            return True
        else:
            return False
