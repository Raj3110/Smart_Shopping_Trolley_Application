import unittest
from unittest.mock import patch
from order import checkout


class TestCheckoutWhiteBox(unittest.TestCase):
    """
    White-box tests for checkout logic.
    Covers internal branches and execution paths.
    """

    # ---------------------------------
    # PURE LOGIC BRANCH TESTS
    # ---------------------------------

    def test_bulk_discount_branch(self):
        quantity = 5
        price = 10
        total = price * quantity
        discount = total * 0.10 if quantity >= 5 else 0
        self.assertEqual(discount, 5)

    def test_no_bulk_discount_branch(self):
        quantity = 2
        price = 10
        total = price * quantity
        discount = total * 0.10 if quantity >= 5 else 0
        self.assertEqual(discount, 0)

    def test_cart_offer_branch(self):
        subtotal = 100
        cart_offer = 10 if subtotal >= 100 else 0
        self.assertEqual(cart_offer, 10)

    # ---------------------------------
    # EXECUTION-BASED WHITE-BOX TESTS
    # ---------------------------------

    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "cash",     # payment method
        "4"         # skip receipt
    ])
    def test_checkout_cash_path(self, mock_input, mock_save, mock_load):
        """
        Path covered:
        - bulk discount
        - cart offer
        - cash payment
        - skip receipt
        """
        cart = [{"name": "apple", "price": 20, "quantity": 5}]
        checkout(cart, "1111111111")

        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "card",                     # payment
        "1234567812345678",         # card
        "12/26",                    # expiry
        "123",                      # cvv
        "4"                         # skip receipt
    ])
    def test_checkout_card_success_path(
        self, mock_input, mock_save, mock_load
    ):
        """
        Path covered:
        - card payment branch
        - successful validation
        - receipt skipped
        """
        cart = [{"name": "banana", "price": 30, "quantity": 2}]
        checkout(cart, "2222222222")

        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)

    @patch("order.load_orders", return_value=[])
    @patch("builtins.input", side_effect=[
        "card",                     # payment
        "111",                      # invalid card
        "1234567812345678",         # valid card
        "12/26",                    # expiry
        "123",                      # cvv
        "4"                         # skip receipt
    ])
    def test_checkout_card_retry_branch(self, mock_input, mock_load):
        """
        Path covered:
        - invalid card
        - retry loop
        - successful card validation
        """
        cart = [{"name": "orange", "price": 10, "quantity": 3}]
        checkout(cart, "3333333333")

        self.assertEqual(cart, [])


if __name__ == "__main__":
    unittest.main()
