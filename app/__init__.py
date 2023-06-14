from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from app.models.project_model import Project
    from app.models.status_model import Status
    from app.models.task_model import Task
    from app.models.user_model import User
    from app.models.user_roles_model import UserRole
    from app.models.user_role_permission_model import UserRolePermission
    from app.models.permission_model import Permission

    db.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(Exception)
    def handle_error(error):
        error_message = f'error: {error}'

        app.logger.error(error_message)
        return jsonify({"error": str(error)}), 500

    return app
