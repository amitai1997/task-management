from flask import Blueprint, jsonify, request
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__, url_prefix="/users")
user_service = UserService()


@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users), 200


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id, ):
    data = request.get_json()
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted'}), 204
    return jsonify({'message': 'User not found'}), 404
