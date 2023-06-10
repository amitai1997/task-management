from flask import Blueprint, jsonify, request
from app.services.project_service import ProjectService

project_bp = Blueprint('project', __name__, url_prefix="/projects")
project_service = ProjectService()


@project_bp.route('/', methods=['GET'])
def get_all_projects():
    projects = project_service.get_all_projects()
    return jsonify(projects), 200


@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    project = project_service.get_project_by_id(project_id)
    if project:
        return jsonify(project), 200
    return jsonify({'message': 'Project not found'}), 404


@project_bp.route('/', methods=['POST'])
def create_project():
    data = request.get_json()
    project = project_service.create_project(data)
    return jsonify(project), 201


@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.get_json()
    project = project_service.update_project(project_id, data)
    if project:
        return jsonify(project), 200
    return jsonify({'message': 'Project not found'}), 404


@project_bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    result = project_service.delete_project(project_id)
    if result:
        return jsonify({'message': 'Project deleted'}), 200
    return jsonify({'message': 'Project not found'}), 404
