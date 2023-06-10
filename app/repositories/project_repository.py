from app.models.project_model import Project
from app import db


class ProjectRepository:
    def get_all_projects(self):
        projects = Project.query.all()
        return [project for project in projects]

    def get_project_by_id(self, project_id):
        project = Project.query.get(project_id)
        if project:
            return project
        else:
            return None

    def create_project(self, data):
        project = Project(title=data['title'], description=data['description'])
        db.session.add(project)
        db.session.commit()
        return project

    def update_project(self, project_id, data):
        project = Project.query.get(project_id)
        if project:
            project.title = data.get('title', project.title)
            project.description = data.get('description', project.description)
            db.session.commit()
            return project
        else:
            return None

    def delete_project(self, project_id):
        project = Project.query.get(project_id)
        if project:
            db.session.delete(project)
            db.session.commit()
            return True
        else:
            return False
