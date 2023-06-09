from app.models.task_model import Task
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@db:5432/task_management'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String)


with app.app_context():
    db.create_all()

# migrate = Migrate(app, db)

# Import the models

# Register the blueprints/controllers here
# from app.controllers.task_controller import task_bp
# from app.controllers.project_controller import project_bp
# app.register_blueprint(task_bp)
# app.register_blueprint(project_bp)


@app.route("/")
def index():
    return "Hello, from task management!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
