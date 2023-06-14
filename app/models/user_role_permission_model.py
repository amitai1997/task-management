from app import db
from dataclasses import dataclass


@dataclass
class UserRolePermission(db.Model):
    __tablename__ = "user_role_permissions"
    user_role_id: int
    permission_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_role_id = db.Column(db.Integer, db.ForeignKey(
        'user_roles.id', ondelete='CASCADE'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey(
        'permissions.id', ondelete='CASCADE'), nullable=False)
