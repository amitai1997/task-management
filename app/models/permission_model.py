from app import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped


@dataclass
class Permission(db.Model):
    __tablename__ = 'permissions'
    id: int
    name: str
    roles: Mapped[str]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    roles = db.relationship('UserRolePermission',
                            cascade='all, delete', backref='permission')

    def __init__(self, name):
        self.name = name
