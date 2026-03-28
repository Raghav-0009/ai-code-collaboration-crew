from datetime import datetime
from typing import Optional

class TransactionError(Exception):
    """Base class for all transaction-related errors."""
    pass

class InsufficientBalanceError(TransactionError):
    """Raised when the user's balance is insufficient to complete the transaction."""
    pass

class Transaction:
    def __init__(self, amount: float, balance: float):
        """
        Initializes a new transaction.

        Args:
        - amount (float): The amount of the transaction.
        - balance (float): The user's current balance.
        """
        self.amount = amount
        self.balance = balance

    def is_valid(self) -> bool:
        """
        Checks if the transaction is valid.

        A transaction is valid if the user's balance is sufficient to complete the transaction.

        Returns:
        - bool: True if the transaction is valid, False otherwise.
        """
        try:
            if self.balance >= self.amount:
                return True
            else:
                raise InsufficientBalanceError("Insufficient balance")
        except InsufficientBalanceError as e:
            raise e

def create_test_transaction(amount: float, balance: float) -> Optional[Transaction]:
    """
    Creates a test transaction.

    Args:
    - amount (float): The amount of the transaction.
    - balance (float): The user's current balance.

    Returns:
    - Transaction: The created transaction, or None if the transaction is invalid.
    """
    try:
        transaction = Transaction(amount, balance)
        if transaction.is_valid():
            return transaction
        else:
            return None
    except InsufficientBalanceError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Initialize a test transaction with an amount of $100 and a balance of $1000
    test_transaction = create_test_transaction(100.0, 1000.0)
    if test_transaction:
        print(f"Test transaction created: amount=${test_transaction.amount}, balance=${test_transaction.balance}")
    else:
        print("Test transaction failed due to insufficient balance.")

    # Initialize a test transaction with an amount of $1500 and a balance of $1000
    test_transaction = create_test_transaction(1500.0, 1000.0)
    if test_transaction:
        print(f"Test transaction created: amount=${test_transaction.amount}, balance=${test_transaction.balance}")
    else:
        print("Test transaction failed due to insufficient balance.")