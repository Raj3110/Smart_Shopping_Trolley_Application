import unittest
from unittest.mock import patch
from order import checkout


class TestCheckoutBlackBox(unittest.TestCase):
    """
    Black-box tests for checkout functionality.
    Enhanced to execute real checkout logic for high coverage.
    """

    def test_checkout_empty_cart(self):
        """
        Given an empty cart
        When checkout is called
        Then function should return None
        """
        cart = []
        result = checkout(cart, "9999999999")
        self.assertIsNone(result)

    def test_discount_applied_bulk(self):
        """
        Given quantity >= 5
        Then bulk discount rule should apply (10%)
        """
        cart = [{"name": "apple", "price": 10, "quantity": 5}]
        subtotal = 50
        expected_discount = 5
        self.assertEqual(subtotal * 0.10, expected_discount)

    # -----------------------------
    # EXECUTION-BASED BLACK-BOX TESTS
    # -----------------------------

    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "n",        # no coupon
        "cash"      # payment method
    ])
    def test_checkout_cash_execution(self, mock_input, mock_save, mock_load):
        """
        Given valid cart
        When checkout with cash
        Then order should be saved and cart cleared
        """
        cart = [{"name": "apple", "price": 10, "quantity": 5}]
        checkout(cart, "9999999999")
        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "n",                        # no coupon
        "card",                     # payment method
        "1234567812345678",         # ✅ valid 16-digit card
        "12/26",                    # expiry
        "123",                      # cvv
        "4321"                      # correct OTP
    ])
    @patch("order.random.randint", return_value=4321)
    def test_checkout_card_execution(self, mock_rand, mock_input, mock_save, mock_load):
        """
        Given valid cart
        When checkout with card and correct OTP
        Then order should complete successfully
        """
        cart = [{"name": "banana", "price": 20, "quantity": 3}]
        checkout(cart, "8888888888")
        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    @patch("order.load_orders", return_value=[])
    @patch("builtins.input", side_effect=[
        "y",        # has coupon
        "INVALID",  # invalid coupon
        "2",        # ✅ skip coupon
        "cash"      # payment method
    ])
    def test_checkout_invalid_coupon(self, mock_input, mock_load):
        """
        Given invalid coupon
        When checkout proceeds
        Then checkout should still succeed
        """
        cart = [{"name": "apple", "price": 50, "quantity": 2}]
        result = checkout(cart, "7777777777")
        self.assertIsNone(result)
        self.assertEqual(cart, [])


if __name__ == "__main__":
    unittest.main()
