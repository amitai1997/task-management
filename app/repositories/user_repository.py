from app import db
from app.models.user_model import User


class UserRepository:
    def get_all_users(self):
        users = User.query.all()
        return [user for user in users]

    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user
        else:
            return None

    def create_user(self, data):
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user_id, data):
        user = User.query.get(user_id)
        if user:
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.password = data.get('password', user.password)
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            db.session.commit()
            return user
        else:
            return None

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False
