from .processor import Processor
from app.repositories.transaction_repository import TransactionRepository


class BillingService:
    def __init__(self):
        self.processor = Processor()
        self.transaction_repo = TransactionRepository()

    def perform_advance(self, dst_bank_account, amount):
        transaction_id = self.processor.perform_transaction(
            src_bank_account="",
            dst_bank_account=dst_bank_account,
            amount=amount,
            direction="credit"
        )
        self.transaction_repo.create_transaction(
            transaction_id, dst_bank_account, amount, "credit")
        return transaction_id

    def perform_debits(self):
        transactions = self.transaction_repo.get_pending_transactions()
        for transaction in transactions:
            try:
                self.processor.perform_transaction(
                    src_bank_account=transaction["dst_bank_account"],
                    dst_bank_account="",
                    amount=transaction["amount"] / 12,
                    direction="debit"
                )
                self.transaction_repo.update_transaction_status(
                    transaction["id"], "success")
            except Exception as e:
                self.transaction_repo.update_transaction_status(
                    transaction["id"], "fail")
                # Move failed transaction to the end of the repayment plan (a week from the last payment)
                self.transaction_repo.move_transaction_to_end(
                    transaction["id"])

    def get_transaction(self, transaction_id):
        return self.transaction_repo.get_transaction(transaction_id)

    def get_all_transactions(self):
        return self.transaction_repo.get_all_transactions()
