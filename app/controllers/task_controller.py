from flask import Blueprint, jsonify, request
from app.services.task_service import TaskService

task_bp = Blueprint('task_bp', __name__, url_prefix="/tasks")
task_service = TaskService()


@task_bp.route('/', methods=['GET'])
def get_all_tasks():
    project_id = None

    if request.is_json:
        data = request.get_json()
        project_id = data.get('project_id')

    if project_id:
        tasks = task_service.get_tasks_by_project(project_id)
    else:
        tasks = task_service.get_all_tasks()

    return jsonify(tasks), 200


@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task_by_id(task_id)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.create_task(data)
    return jsonify(task), 201


@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_service.update_task(task_id, data)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@task_bp.route('/<int:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    new_status = None

    if request.is_json:
        data = request.get_json()
        new_status = data.get('status')

    if new_status:
        task = task_service.update_task_status(task_id, new_status)
    else:
        return jsonify({'error': f'field "{list(data.keys())[0]}" not found'}), 404
    if task:
        return jsonify(task), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = task_service.delete_task(task_id)
    if result:
        return jsonify({'message': 'Task deleted'}), 204
    else:
        return jsonify({'error': 'Task not found'}), 404
