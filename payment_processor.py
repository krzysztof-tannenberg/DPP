from transaction import TransactionResult, TransactionStatus
from exceptions import NetworkException, PaymentException, RefundException

class PaymentGateway:
    def charge(self, user_id: str, amount: float) -> TransactionResult:
        raise NotImplementedError("This is an interface method.")

    def refund(self, transaction_id: str) -> TransactionResult:
        raise NotImplementedError("This is an interface method.")

    def get_status(self, transaction_id: str) -> TransactionStatus:
        raise NotImplementedError("This is an interface method.")

class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, user_id: str, amount: float, retries: int = 1) -> TransactionResult:
        if not user_id or amount <= 0:
            raise ValueError("Invalid user_id or amount.")
        for attempt in range(retries + 1):  # Próba początkowa + określona liczba retry
            try:
                result = self.payment_gateway.charge(user_id, amount)
                return result
            except NetworkException as e:
                if attempt < retries:
                    # Logowanie i kontynuacja kolejnej próby
                    print(f"Retrying payment for user {user_id} after network error: {e}")
                    continue
                else:
                    # Ostateczny wyjątek po wyczerpaniu retry
                    print(f"Payment failed for user {user_id} after {retries} retries.")
                    raise e

    def refund_payment(self, transaction_id: str) -> TransactionResult:
        if not transaction_id:
            raise ValueError("Invalid transaction_id.")
        try:
            result = self.payment_gateway.refund(transaction_id)
            return result
        except (NetworkException, RefundException) as e:
            # Log exception and rethrow or handle
            raise e

    def get_payment_status(self, transaction_id: str) -> TransactionStatus:
        if not transaction_id:
            raise ValueError("Invalid transaction_id.")
        try:
            status = self.payment_gateway.get_status(transaction_id)
            return status
        except NetworkException as e:
            # Log exception and rethrow or handle
            raise e
