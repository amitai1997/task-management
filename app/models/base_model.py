from sqlalchemy.orm import class_mapper
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=True, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def serialize(self):
        columns = [c.key for c in class_mapper(self.__class__).columns]

        columns.remove('created_at') if not self.created_at else columns
        columns.remove('updated_at') if not self.updated_at else columns

        return dict((c, getattr(self, c)) for c in columns)
