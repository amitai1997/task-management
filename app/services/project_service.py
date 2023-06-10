from app.repositories.project_repository import ProjectRepository


class ProjectService:
    def __init__(self):
        self.project_repo = ProjectRepository()

    def get_all_projects(self):
        return self.project_repo.get_all_projects()

    def get_project_by_id(self, project_id):
        return self.project_repo.get_project_by_id(project_id)

    def create_project(self, data):
        return self.project_repo.create_project(data)

    def update_project(self, project_id, data):
        return self.project_repo.update_project(project_id, data)

    def delete_project(self, project_id):
        return self.project_repo.delete_project(project_id)
