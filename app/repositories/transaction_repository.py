import psycopg2
from app.app import app
from app.utils.database import get_db_connection
from flask import current_app


class TransactionRepository:
    def __init__(self):
        self.connection = get_db_connection()

    def create_transaction(self, transaction_id, dst_bank_account, amount, direction):
        query = """
        INSERT INTO transactions (id, dst_bank_account, amount, direction)
        VALUES (%s, %s, %s, %s)
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                query, (transaction_id, dst_bank_account, amount, direction))
        self.connection.commit()

    def get_transaction(self, transaction_id):
        query = """
        SELECT transaction_id, dst_bank_account, amount, direction, status
        FROM transactions
        WHERE transaction_id = %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (transaction_id,))
            return cursor.fetchone()

    def get_all_transactions(self):
        query = """
        SELECT transaction_id, dst_bank_account, amount, direction, status
        FROM transactions
        ORDER BY transaction_id
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_pending_transactions(self):
        query = """
        SELECT id, dst_bank_account, amount
        FROM transactions
        WHERE status = 'pending'
        ORDER BY id
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def update_transaction_status(self, transaction_id, status):
        query = """
        UPDATE transactions
        SET status = %s
        WHERE transaction_id = %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (status, transaction_id))
        self.connection.commit()

    def move_transaction_to_end(self, transaction_id):
        query = """
        UPDATE transactions
        SET created_at = now() + INTERVAL '1 week'
        WHERE transaction_id = %s
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query, (transaction_id,))
        self.connection.commit()
