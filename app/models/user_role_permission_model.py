from app import db
from dataclasses import dataclass
from .base_model import BaseModel


@dataclass
class UserRolePermission(db.Model, BaseModel):
    __tablename__ = "user_role_permissions"
    user_role_id: int
    permission_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_role_id = db.Column(db.Integer, db.ForeignKey(
        'user_roles.id', ondelete='CASCADE'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey(
        'permissions.id', ondelete='CASCADE'), nullable=False)

    def serialize(self) -> dict:
        serialized_model = super().serialize()
        serialized_model['permission'] = self.permission.name if self.permission_id else None
        serialized_model['user_role'] = self.role.name if self.role.name else None
        serialized_model.pop('permission_id', None)
        serialized_model.pop('user_role_id', None)
        return serialized_model
