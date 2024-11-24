import unittest
from unittest.mock import MagicMock, call
from payment_processor import PaymentProcessor, PaymentGateway
from transaction import TransactionResult, TransactionStatus
from exceptions import NetworkException, PaymentException, RefundException

class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.mock_gateway = MagicMock(spec=PaymentGateway)
        self.processor = PaymentProcessor(self.mock_gateway)

    def test_process_payment_success(self):
        # Arrange
        user_id = "Krzysztof"
        amount = 100.0
        transaction_result = TransactionResult(success=True, transaction_id="platnosc321")
        self.mock_gateway.charge.return_value = transaction_result

        # Act
        print(f"\nTesting process_payment for user_id={user_id}, amount={amount}")
        result = self.processor.process_payment(user_id, amount)

        # Assert
        self.mock_gateway.charge.assert_called_once_with(user_id, amount)
        self.assertTrue(result.success)
        self.assertEqual(result.transaction_id, "platnosc321")
        print(f"\nTest process_payment_success passed!")

    def test_process_payment_failure_due_to_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment("Krzysztof", -10)

    def test_process_payment_failure_network_exception(self):
        self.mock_gateway.charge.side_effect = NetworkException("Network error")
        with self.assertRaises(NetworkException):
            self.processor.process_payment("Krzysztof", 100.0)

    def test_refund_payment_success(self):
        # Arrange
        transaction_id = "platnosc321"
        transaction_result = TransactionResult(success=True, transaction_id=transaction_id)
        self.mock_gateway.refund.return_value = transaction_result

        # Act
        result = self.processor.refund_payment(transaction_id)

        # Assert
        self.mock_gateway.refund.assert_called_once_with(transaction_id)
        self.assertTrue(result.success)

    def test_get_payment_status(self):
        # Arrange
        transaction_id = "platnosc321"
        self.mock_gateway.get_status.return_value = TransactionStatus.COMPLETED

        # Act
        status = self.processor.get_payment_status(transaction_id)

        # Assert
        self.mock_gateway.get_status.assert_called_once_with(transaction_id)
        self.assertEqual(status, TransactionStatus.COMPLETED)

    def test_log_and_retry_on_network_exception(self):
        user_id = "Krzysztof"
        amount = 100.0
        self.mock_gateway.charge.side_effect = [
            NetworkException("Network error"),
            TransactionResult(success=True, transaction_id="platnosc321")
        ]

        print("Starting test_log_and_retry_on_network_exception...")
        result = self.processor.process_payment(user_id, amount, retries=1)
        self.mock_gateway.charge.assert_called_with(user_id, amount)

        # Logowanie liczby wywołań
        print(f"Gateway charge called {self.mock_gateway.charge.call_count} times.")
        self.assertEqual(self.mock_gateway.charge.call_count, 2)
        print("Result of payment: Success =", result.success, ", Transaction ID =", result.transaction_id)
        print("Test log_and_retry_on_network_exception passed!")

# Wywołanie
# python -m unittest -v test_payment_processor.py
