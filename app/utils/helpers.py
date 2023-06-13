from flask import jsonify
from sqlalchemy.orm import class_mapper
import json


def serialize_model(model):
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
