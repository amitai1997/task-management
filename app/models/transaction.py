from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, success):
        self.transaction_id = transaction_id
        self.success = success
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'success': self.success,
            'timestamp': self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            transaction_id=data['transaction_id'],
            success=data['success']
        )
