from flask import Flask
from flask.cli import AppGroup
from flask_migrate import Migrate, upgrade
from alembic import op
import sqlalchemy as sa


def custom_upgrade_command(app):
    with app.app_context():
        op.add_column('tasks', sa.Column('status_new', sa.Integer()))
        op.execute(
            "UPDATE tasks SET status_new = CASE status WHEN 'value1' THEN 1 WHEN 'value2' THEN 2 ELSE 0 END")
        op.drop_column('tasks', 'status')
        op.alter_column('tasks', 'status_new', new_column_name='status',
                        existing_type=sa.Integer(), nullable=False)

        upgrade()
