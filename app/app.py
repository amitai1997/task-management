import os
# from app.controllers.user_controller import user_bp
from app.controllers.user_role_controller import user_role_bp
from app.controllers.user_role_permission_controller import user_role_permission_bp
from app.controllers.controllers import *

from . import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# Register the blueprints/controllers here
# app.register_blueprint(user_bp)
app.register_blueprint(user_role_bp)
app.register_blueprint(user_role_permission_bp)

aaa_bp = AaaAPI('aaa_bp', __name__, url_prefix="/aaa")
permission_bp = PermissionAPI(
    'permission_bp', __name__, url_prefix="/permissions")
project_bp = ProjectAPI(
    'project_bp', __name__, url_prefix="/projects")
status_bp = StatusAPI(
    'status_bp', __name__, url_prefix="/statuses")
task_bp = TaskAPI(
    'task_db', __name__, url_prefix="/tasks")
user_bp = UserAPI(
    'user_db', __name__, url_prefix="/users")

app.register_blueprint(aaa_bp)
app.register_blueprint(permission_bp)
app.register_blueprint(project_bp)
app.register_blueprint(status_bp)
app.register_blueprint(task_bp)
app.register_blueprint(user_bp)


@app.route("/")
def index():
    return "Hello, from task management!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
