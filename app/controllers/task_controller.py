from flask import Blueprint, jsonify, request
from app.models.task_model import Task
from app.repositories.task_repository import TaskRepository

task_bp = Blueprint('task_bp', __name__, url_prefix="/tasks")
task_repo = TaskRepository()


@task_bp.route('/', methods=['GET'])
def get_all_tasks():
    tasks = task_repo.get_all_tasks()
    return jsonify(tasks), 200


@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_repo.get_task_by_id(task_id)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_repo.create_task(data)
    return jsonify(task), 201


@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_repo.update_task(task_id, data)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({'error': 'Task not found'}), 404


@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = task_repo.delete_task(task_id)
    if result:
        return '', 204
    else:
        return jsonify({'error': 'Task not found'}), 404
