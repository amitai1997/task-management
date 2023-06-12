from app.models.status_model import Status
from app import db


class StatusRepository:
    def get_all_statuses(self):
        statuses = Status.query.all()
        return [status for status in statuses]

    def get_status_by_id(self, status_id):
        status = Status.query.get(status_id)
        if status:
            return status
        else:
            return None

    def create_status(self, data):
        status = Status(title=data['title'])
        db.session.add(status)
        db.session.commit()
        return status

    def update_status(self, status_id, data):
        status = Status.query.get(status_id)
        if status:
            status.title = data.get('title', status.title)
            db.session.commit()
            return status
        else:
            return None

    def delete_status(self, status_id):
        status = Status.query.get(status_id)
        if status:
            db.session.delete(status)
            db.session.commit()
            return True
        else:
            return False
