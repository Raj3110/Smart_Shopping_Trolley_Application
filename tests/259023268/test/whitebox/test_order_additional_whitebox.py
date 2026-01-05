import unittest
from unittest.mock import patch
from order import checkout


class TestOrderAdditionalWhiteBox(unittest.TestCase):
    """
    White-box tests to cover advanced checkout branches:
    - loyalty discount
    - coupon logic
    - tax calculation
    - card payment
    - receipt selection paths
    """

    # --------------------------------------------------
    # LOYALTY + CASH + RECEIPT PRINT
    # --------------------------------------------------
    @patch("order.load_orders", return_value=[
        {"customer": "1111111111", "total": 40},
        {"customer": "1111111111", "total": 60},
        {"customer": "1111111111", "total": 30}
    ])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "cash",     # payment method
        "1"         # receipt → print on screen
    ])
    def test_loyal_customer_cash_with_print_receipt(
        self, mock_input, mock_save, mock_load
    ):
        """
        Covers:
        - loyalty discount
        - tax calculation
        - cash payment
        - print receipt branch
        """
        cart = [
            {"name": "apple", "price": 10, "quantity": 4},
            {"name": "banana", "price": 5, "quantity": 6}
        ]

        checkout(cart, "1111111111")

        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    # --------------------------------------------------
    # CARD PAYMENT SUCCESS + SAVE TEXT RECEIPT
    # --------------------------------------------------
    @patch("order.random.randint", return_value=1234)
    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "card",                     # payment method
        "1234567812345678",         # valid card
        "12/26",                    # expiry
        "123",                      # cvv
        "2"                         # receipt → save as text
    ])
    def test_card_payment_with_text_receipt(
        self, mock_input, mock_save, mock_load, mock_rand
    ):
        """
        Covers:
        - card payment validation
        - tax calculation
        - text receipt save path
        """
        cart = [{"name": "milk", "price": 30, "quantity": 2}]
        checkout(cart, "2222222222")

        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    # --------------------------------------------------
    # INVALID COUPON → SKIP → CASH → SKIP RECEIPT
    # --------------------------------------------------
    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "cash",     # payment
        "4"         # receipt → skip
    ])
    def test_skip_receipt_path(
        self, mock_input, mock_save, mock_load
    ):
        """
        Covers:
        - skip receipt branch
        """
        cart = [{"name": "bread", "price": 25, "quantity": 1}]
        checkout(cart, "3333333333")

        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)


if __name__ == "__main__":
    unittest.main()
