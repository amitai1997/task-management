import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from app.config import config
from app.models.base_model import Base
from app.auth.decorators import RBACAuthenticator
import redis
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()
authenticator = RBACAuthenticator()
r = redis.Redis(os.getenv('REDIS_CONFIG'), os.getenv('REDIS_PORT'), decode_responses=True)
cache = Cache()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_models(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)
    authenticator.init_app(app)
    cache.init_app(app, config={'CACHE_REDIS_CLIENT': r})


def register_blueprints(app):
    from app.utils.blueprints import register_blueprints
    register_blueprints(app)


def register_error_handlers(app):
    @app.errorhandler(500)
    def handle_internal_server_error(error):
        error_message = f'Error: {error}'
        app.logger.error(error_message)
        return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(Exception)
    def handle_error(error):
        error_message = f'Error: {error}'
        app.logger.error(error_message)
        return jsonify({"error": str(error)}), 500


def register_models(app):
    with app.app_context():

        # Import and register your models here
        from app.models.project_model import Project
        from app.models.status_model import Status
        from app.models.task_model import Task
        from app.models.user_model import User
        from app.models.user_roles_model import UserRole
        from app.models.user_role_permission_model import UserRolePermission
        from app.models.permission_model import Permission

        Base.metadata.create_all(bind=db.engine)
