from flask import jsonify
from sqlalchemy.orm import class_mapper
import json


def serialize_model(model):
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def process_response(value, success_code=200, error_code=404):
    if isinstance(value, dict) or isinstance(value, list):
        return jsonify(value), success_code
    elif isinstance(value, str):
        error_data = {'error': value}
        return jsonify(error_data), error_code
    else:
        return jsonify({'error': 'Unexpected response type'}), error_code
