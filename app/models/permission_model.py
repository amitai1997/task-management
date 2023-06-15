from app import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from .base_model import BaseModel


@dataclass
class Permission(db.Model, BaseModel):
    __tablename__ = 'permissions'
    id: int
    name: str
    roles: Mapped[str]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    roles = db.relationship('UserRolePermission',
                            cascade='all, delete', backref='permission')

    def serialize(self) -> dict:
        serialized_model = super().serialize()
        serialized_model['roles'] = [
            [role.serialize()["permission"], role.serialize()["user_role"]] for role in self.roles] if self.roles else None
        return serialized_model
