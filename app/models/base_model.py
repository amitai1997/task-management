from app import db
from sqlalchemy.orm import class_mapper
from dataclasses import dataclass


class BaseModel():

    def serialize(self):
        columns = [c.key for c in class_mapper(self.__class__).columns]
        return dict((c, getattr(self, c)) for c in columns)
