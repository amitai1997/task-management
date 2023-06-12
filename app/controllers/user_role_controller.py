from flask import Blueprint, jsonify, request
from app.services.user_role_service import UserRoleService

user_role_bp = Blueprint('user_role', __name__, url_prefix="/user-roles")
user_role_service = UserRoleService()


@user_role_bp.route('/', methods=['GET'])
def get_all_user_roles():
    user_roles = user_role_service.get_all_user_roles()
    return jsonify(user_roles), 200


@user_role_bp.route('/<int:user_role_id>', methods=['GET'])
def get_user_role_by_id(user_role_id):
    user_role = user_role_service.get_user_role_by_id(user_role_id)
    if user_role:
        return jsonify(user_role), 200
    return jsonify({'message': 'User role not found'}), 404


@user_role_bp.route('/', methods=['POST'])
def create_user_role():
    data = request.get_json()
    user_role = user_role_service.create_user_role(data)
    return jsonify(user_role), 201


@user_role_bp.route('/<int:user_role_id>', methods=['PUT'])
def update_user_role(user_role_id):
    data = request.get_json()
    user_role = user_role_service.update_user_role(user_role_id, data)
    if user_role:
        return jsonify(user_role), 200
    return jsonify({'message': 'User role not found'}), 404


@user_role_bp.route('/<int:user_role_id>', methods=['DELETE'])
def delete_user_role(user_role_id):
    success = user_role_service.delete_user_role(user_role_id)
    if success:
        return jsonify({'message': 'User role deleted'}), 204
    return jsonify({'message': 'User role not found'}), 404
