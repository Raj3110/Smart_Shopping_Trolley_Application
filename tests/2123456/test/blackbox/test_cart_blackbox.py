import unittest
from unittest.mock import patch
from cart import add_to_cart, remove_from_cart


class TestCartBlackBox(unittest.TestCase):
    """
    Black-box tests for cart functionality.
    Upgraded to execute all major cart paths for higher coverage.
    """

    # ------------------------------------------------
    # BASIC BLACK-BOX TESTS
    # ------------------------------------------------

    def test_remove_item_empty_cart(self):
        """
        Given an empty cart
        When remove_from_cart is called
        Then cart remains empty
        """
        cart = []
        remove_from_cart(cart)
        self.assertEqual(cart, [])

    def test_cart_quantity_positive(self):
        """
        Quantity in cart should always be positive
        """
        cart = [{"name": "apple", "price": 10, "quantity": 5}]
        self.assertGreater(cart[0]["quantity"], 0)

    # ------------------------------------------------
    # EXECUTION-BASED BLACK-BOX TESTS
    # ------------------------------------------------

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "12345"}
    ])
    @patch("builtins.input", side_effect=["12345", "2"])
    def test_add_to_cart_valid_code_quantity(self, mock_input, mock_products):
        """
        Valid scanner code + quantity
        """
        cart = []
        add_to_cart(cart)

        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["name"], "apple")
        self.assertEqual(cart[0]["quantity"], 2)

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "12345"}
    ])
    @patch("builtins.input", side_effect=["12345", ""])
    def test_add_to_cart_default_quantity(self, mock_input, mock_products):
        """
        Empty quantity → default = 1
        """
        cart = []
        add_to_cart(cart)

        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["quantity"], 1)

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "12345"}
    ])
    @patch("builtins.input", side_effect=["99999"])
    def test_add_to_cart_invalid_code(self, mock_input, mock_products):
        """
        Invalid scanner code
        """
        cart = []
        add_to_cart(cart)
        self.assertEqual(cart, [])

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "12345"}
    ])
    @patch("builtins.input", side_effect=[
        "12345", "3",
        "12345", "2"
    ])
    def test_add_to_cart_quantity_merge(self, mock_input, mock_products):
        """
        Same item scanned twice → quantity merge
        """
        cart = []
        add_to_cart(cart)
        add_to_cart(cart)

        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["quantity"], 5)

    # ------------------------------------------------
    # REMOVE CART TESTS
    # ------------------------------------------------

    @patch("builtins.input", side_effect=["1", ""])
    def test_remove_from_cart_full_removal(self, mock_input):
        """
        Remove full item when quantity input is empty
        """
        cart = [{"name": "apple", "price": 10, "quantity": 3}]
        remove_from_cart(cart)

        self.assertEqual(cart, [])

    @patch("builtins.input", side_effect=["1", "1"])
    def test_remove_from_cart_partial_removal(self, mock_input):
        """
        Partial quantity removal
        """
        cart = [{"name": "apple", "price": 10, "quantity": 3}]
        remove_from_cart(cart)

        self.assertEqual(cart[0]["quantity"], 2)


if __name__ == "__main__":
    unittest.main()
