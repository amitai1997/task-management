from flask import Blueprint, jsonify, request
from app.services.status_service import StatusService

status_bp = Blueprint('status', __name__, url_prefix="/statuses")
status_service = StatusService()


@status_bp.route('/', methods=['GET'])
def get_all_statuses():
    statuses = status_service.get_all_statuses()
    return jsonify(statuses), 200


@status_bp.route('/<int:status_id>', methods=['GET'])
def get_status_by_id(status_id):
    status = status_service.get_status_by_id(status_id)
    if status:
        return jsonify(status), 200
    return jsonify({'message': 'Status not found'}), 404


@status_bp.route('/', methods=['POST'])
def create_status():
    data = request.get_json()
    status = status_service.create_status(data)
    return jsonify(status), 201


@status_bp.route('/<int:status_id>', methods=['PUT'])
def update_status(status_id):
    data = request.get_json()
    status = status_service.update_status(status_id, data)
    if status:
        return jsonify(status), 200
    return jsonify({'message': 'Status not found'}), 404


@status_bp.route('/<int:status_id>', methods=['DELETE'])
def delete_status(status_id):
    result = status_service.delete_status(status_id)
    if result:
        return jsonify({'message': 'Status deleted'}), 204
    return jsonify({'message': 'Status not found'}), 404
