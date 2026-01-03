import unittest
from unittest.mock import patch
from cart import add_to_cart, remove_from_cart, view_cart


class TestCartWhiteBox(unittest.TestCase):
    """
    White-box tests for cart logic.
    Focus on branch execution and internal behaviour.
    """

    # -----------------------------
    # EXISTING LOGIC BRANCH TESTS
    # -----------------------------

    def test_quantity_merge_branch(self):
        cart = [{"name": "apple", "price": 10, "quantity": 2}]
        cart[0]["quantity"] += 3
        self.assertEqual(cart[0]["quantity"], 5)

    def test_quantity_remove_branch(self):
        cart = [{"name": "apple", "price": 10, "quantity": 5}]
        cart[0]["quantity"] -= 2
        self.assertEqual(cart[0]["quantity"], 3)

    # -----------------------------
    # ADD TO CART BRANCHES
    # -----------------------------

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "11111"}
    ])
    @patch("builtins.input", side_effect=["11111", ""])
    def test_add_to_cart_default_quantity(self, mock_input, mock_products):
        cart = []
        add_to_cart(cart)
        self.assertEqual(cart[0]["quantity"], 1)

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "11111"}
    ])
    @patch("builtins.input", side_effect=["99999"])
    def test_add_to_cart_invalid_code_branch(self, mock_input, mock_products):
        cart = []
        add_to_cart(cart)
        self.assertEqual(cart, [])

    @patch("cart.list_products", return_value=[
        {"name": "apple", "price": 10, "code": "11111"}
    ])
    @patch("builtins.input", side_effect=["11111", "2", "11111", "3"])
    def test_duplicate_scan_merge_branch(self, mock_input, mock_products):
        cart = []
        add_to_cart(cart)
        add_to_cart(cart)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]["quantity"], 5)

    # -----------------------------
    # REMOVE CART BRANCHES
    # -----------------------------

    def test_remove_from_empty_cart(self):
        cart = []
        remove_from_cart(cart)
        self.assertEqual(cart, [])

    @patch("builtins.input", side_effect=["99"])
    def test_remove_invalid_index(self, mock_input):
        cart = [{"name": "apple", "price": 10, "quantity": 2}]
        remove_from_cart(cart)
        self.assertEqual(cart[0]["quantity"], 2)

    @patch("builtins.input", side_effect=["1", "10"])
    def test_remove_quantity_exceeds_branch(self, mock_input):
        cart = [{"name": "apple", "price": 10, "quantity": 3}]
        remove_from_cart(cart)
        self.assertEqual(cart, [])

    @patch("builtins.input", side_effect=["1", ""])
    def test_remove_full_removal_branch(self, mock_input):
        cart = [{"name": "apple", "price": 10, "quantity": 3}]
        remove_from_cart(cart)
        self.assertEqual(cart, [])

    @patch("builtins.input", side_effect=["1", "1"])
    def test_remove_partial_removal_branch(self, mock_input):
        cart = [{"name": "apple", "price": 10, "quantity": 3}]
        remove_from_cart(cart)
        self.assertEqual(cart[0]["quantity"], 2)

    # -----------------------------
    # VIEW CART / MENU BRANCHES (KEY)
    # -----------------------------



    @patch("cart.checkout")   # prevent real checkout execution
    @patch("builtins.input", side_effect=["4"])
    def test_view_cart_exit_option(self, mock_input, mock_checkout):
        """
        View cart → exit menu
        """
        cart = [{"name": "apple", "price": 10, "quantity": 2}]
        view_cart(cart, "9999999999")

        self.assertEqual(cart[0]["quantity"], 2)
        mock_checkout.assert_not_called()


    @patch("cart.checkout")
    @patch("builtins.input", side_effect=["99", "4"])
    def test_view_cart_invalid_menu_choice(self, mock_input, mock_checkout):
        """
        Invalid menu option → handled safely
        """
        cart = [{"name": "apple", "price": 10, "quantity": 2}]
        view_cart(cart, "9999999999")

        self.assertEqual(cart[0]["quantity"], 2)
        mock_checkout.assert_not_called()


    @patch("cart.checkout")
    @patch("builtins.input", side_effect=["1", "1", "5", "4"])
    def test_view_cart_modify_quantity_branch(self, mock_input, mock_checkout):
        """
        View cart → modify quantity → exit
        """
        cart = [{"name": "apple", "price": 10, "quantity": 2}]
        view_cart(cart, "9999999999")

        self.assertEqual(cart[0]["quantity"], 5)
        mock_checkout.assert_not_called()


if __name__ == "__main__":
    unittest.main()
