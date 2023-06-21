from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from app.config import config
from app.models.base_model import Base

db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_oauth(app)
    with app.app_context():
        register_models()

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    from app.utils.blueprints import register_blueprints
    register_blueprints(app)


def register_oauth(app):
    from app.utils.auth import register_oauth
    register_oauth(app)


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_error(error):
        error_message = f'Error: {error}'
        app.logger.error(error_message)
        return jsonify({"error": str(error)}), 500


def register_models():
    from app import db

    # Import and register your models here
    from app.models.project_model import Project
    from app.models.status_model import Status
    from app.models.task_model import Task
    from app.models.user_model import User
    from app.models.user_roles_model import UserRole
    from app.models.user_role_permission_model import UserRolePermission
    from app.models.permission_model import Permission

    Base.metadata.create_all(bind=db.engine)
