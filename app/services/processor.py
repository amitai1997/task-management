import random
import string


class Processor:
    def __init__(self):
        # Initialize any necessary attributes or dependencies
        pass

    def perform_transaction(self, src_bank_account, dst_bank_account, amount, direction):
        # Generate a unique transaction ID
        transaction_id = self._generate_transaction_id()

        # Perform the transaction logic here
        # Placeholder logic: Print the transaction details
        print(f"Performing {direction} transaction:")
        print(f"Transaction ID: {transaction_id}")
        print(f"Source Bank Account: {src_bank_account}")
        print(f"Destination Bank Account: {dst_bank_account}")
        print(f"Amount: {amount}")

        # Return the transaction ID
        return transaction_id

    def _generate_transaction_id(self):
        # Generate a random alphanumeric transaction ID
        # TODO change the id colum to string/hash
        # return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        random_number = ''.join(random.choices(string.digits, k=8))
        random_number = int(random_number)
        return random_number
