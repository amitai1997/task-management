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
from flask_session import Session

db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()
authenticator = RBACAuthenticator()
r = None
cache = Cache()
session = Session()


def create_app(config_name):
    """
    Create a Flask application with the specified configuration.

    Args:
        config_name (str): The name of the configuration.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    configure_app(app, config_name)
    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_models(app)

    return app


def configure_app(app, config_name):
    """
    Configure the Flask application with the specified configuration.

    Args:
        app (Flask): The Flask application instance.
        config_name (str): The name of the configuration.
    """
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


def register_extensions(app):
    """
    Register Flask extensions with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    db.init_app(app)
    migrate.init_app(app, db)
    oauth.init_app(app)
    authenticator.init_app(app)
    global r
    r = init_redis(app)  # Assign Redis instance to r
    cache.init_app(app, config={'CACHE_REDIS_CLIENT': r})
    session.init_app(app)


def init_redis(app):
    return redis.Redis(
        host=app.config['REDIS_HOST'],
        port=app.config['REDIS_PORT'],
        decode_responses=True
    )


def register_blueprints(app):
    """
    Register blueprints with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    from app.utils.blueprints import register_blueprints
    register_blueprints(app)


def register_error_handlers(app):
    """
    Register error handlers with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    @app.errorhandler(500)
    def handle_internal_server_error(error):
        """
        Handle internal server errors (HTTP 500).

        Args:
            error (Exception): The error that occurred.

        Returns:
            tuple: A tuple containing the response body and status code.
        """
        error_message = f'Error: {error}'
        app.logger.error(error_message)
        return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(Exception)
    def handle_error(error):
        """
        Handle general exceptions.

        Args:
            error (Exception): The exception that occurred.

        Returns:
            tuple: A tuple containing the response body and status code.
        """
        error_message = f'Error: {error}'
        app.logger.error(error_message)
        return jsonify({"error": str(error)}), 500


def register_models(app):
    """
    Register models with the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
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
