from flask import Blueprint, jsonify, request
from app.services.permission_service import PermissionService

permission_bp = Blueprint('permission_bp', __name__, url_prefix="/permissions")
permission_service = PermissionService()


@permission_bp.route('/', methods=['GET'])
def get_all_permissions():
    data = {}

    if request.is_json:
        data = request.get_json()

    permissions = permission_service.get_all_permissions(data)

    return jsonify(permissions), 200


@permission_bp.route('/<int:permission_id>', methods=['GET'])
def get_permission(permission_id):
    permission = permission_service.get_permission_by_id(permission_id)
    if permission:
        return jsonify(permission), 200
    else:
        return jsonify({'error': 'Permission not found'}), 404


@permission_bp.route('/', methods=['POST'])
def create_permission():
    data = request.get_json()
    permission = permission_service.create_permission(data)
    return jsonify(permission), 201


@permission_bp.route('/<int:permission_id>', methods=['PUT'])
def update_permission(permission_id):
    data = request.get_json()
    permission = permission_service.update_permission(permission_id, data)
    if permission:
        return jsonify(permission), 200
    else:
        return jsonify({'error': 'Permission not found'}), 404


@permission_bp.route('/<int:permission_id>', methods=['DELETE'])
def delete_permission(permission_id):
    result = permission_service.delete_permission(permission_id)
    if result:
        return jsonify({'message': 'Permission deleted'}), 204
    else:
        return jsonify({'error': 'Permission not found'}), 404
