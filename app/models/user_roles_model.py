from app import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped


@dataclass
class UserRole(db.Model):
    __tablename__ = "user_roles"
    id: int
    name: str
    description: str
    permissions: Mapped[str]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(256))
    permissions = db.relationship(
        'UserRolePermission', cascade='all, delete', backref='role')
