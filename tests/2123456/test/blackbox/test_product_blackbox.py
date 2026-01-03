import unittest
from unittest.mock import patch
from product import add_product, update_product


class TestProductBlackBox(unittest.TestCase):
    """
    Black-box execution tests for admin product management.
    """

    @patch("product.save_products")
    @patch("product.load_products", return_value=[])
    @patch("builtins.input", side_effect=["apple", "10", "12345"])
    def test_add_product_execution(self, mock_input, mock_load, mock_save):
        """
        Given valid product details
        When add_product is executed
        Then product should be saved
        """
        add_product()
        self.assertTrue(mock_save.called)

    @patch("product.save_products")
    @patch("product.load_products", return_value=[
        {"name": "apple", "price": 10, "code": "12345"}
    ])
    @patch("builtins.input", side_effect=[
        "1",        # select product
        "banana",   # new name
        "20",       # new price
        ""          # keep same code
    ])
    def test_update_product_execution(self, mock_input, mock_load, mock_save):
        """
        Given existing product
        When update_product is executed
        Then updated product should be saved
        """
        update_product()
        self.assertTrue(mock_save.called)


if __name__ == "__main__":
    unittest.main()
