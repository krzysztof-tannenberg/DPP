from enum import Enum

class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class TransactionResult:
    def __init__(self, success: bool, transaction_id: str, message: str = ""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
