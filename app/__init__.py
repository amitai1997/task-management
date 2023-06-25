from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.integrations.flask_client import OAuth
from app.config import config
from app.models.base_model import Base
from app.security.auth0_service import Auth0Service
from app.utils import safe_get_env_var
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
oauth = OAuth()
auth0_service = Auth0Service()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.url_map.strict_slashes = False

    register_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)
    register_oauth(app)
    register_cors(app)
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
    auth0_audience = safe_get_env_var("API_IDENTIFIER")
    auth0_domain = safe_get_env_var("AUTH0_DOMAIN")

    register_oauth(app)
    auth0_service.initialize(auth0_domain, auth0_audience)


def register_cors(app):
    client_origin_url = safe_get_env_var("CLIENT_ORIGIN_URL")
    CORS(
        app,
        resources={r"/*": {"origins": "*"}}
        #     allow_headers=["Authorization", "Content-Type"],
        #     methods=["GET"],
        #     max_age=86400
    )


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
