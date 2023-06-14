from flask import Blueprint, jsonify, request
from app.services.user_role_permission_service import UserRolePermissionService


user_role_permission_bp = Blueprint(
    'user_role_permission_bp', __name__, url_prefix="/user-role-permissions")
user_role_permission_service = UserRolePermissionService()


@user_role_permission_bp.route('/', methods=['GET'])
def get_all_user_role_permissions():
    data = {}

    if request.is_json:
        data = request.get_json()

    user_role_permissions = user_role_permission_service.get_all_user_role_permissions(
        data)

    return jsonify(user_role_permissions), 200


@user_role_permission_bp.route('/<int:user_role_permission_id>', methods=['GET'])
def get_user_role_permission(user_role_permission_id):
    user_role_permission = user_role_permission_service.get_user_role_permission_by_id(
        user_role_permission_id)
    if user_role_permission:
        return jsonify(user_role_permission), 200
    else:
        return jsonify({'error': 'User Role Permission not found'}), 404


@user_role_permission_bp.route('/', methods=['POST'])
def create_user_role_permission():
    data = request.get_json()
    user_role_permission = user_role_permission_service.create_user_role_permission(
        data)
    return jsonify(user_role_permission), 201


@user_role_permission_bp.route('/<int:user_role_permission_id>', methods=['PUT'])
def update_user_role_permission(user_role_permission_id):
    data = request.get_json()
    user_role_permission = user_role_permission_service.update_user_role_permission(
        user_role_permission_id, data)
    if user_role_permission:
        return jsonify(user_role_permission), 200
    else:
        return jsonify({'error': 'User Role Permission not found'}), 404


@user_role_permission_bp.route('/<int:user_role_permission_id>', methods=['DELETE'])
def delete_user_role_permission(user_role_permission_id):
    result = user_role_permission_service.delete_user_role_permission(
        user_role_permission_id)
    if result:
        return jsonify({'message': 'User Role Permission deleted'}), 204
    else:
        return jsonify({'error': 'User Role Permission not found'}), 404
