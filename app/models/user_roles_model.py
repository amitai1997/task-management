from app import db


class UserRole(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(256))
    permissions = db.Column(db.String(256))

    def __init__(self, name, description, permissions):
        self.name = name
        self.description = description
        self.permissions = permissions
