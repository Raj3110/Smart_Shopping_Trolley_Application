import unittest
from unittest.mock import patch, mock_open
from storage import log_event, save_products, load_products


class TestStorageWhiteBox(unittest.TestCase):
    """
    White-box execution tests for storage utilities.
    """

    @patch("builtins.open", new_callable=mock_open)
    def test_log_event_execution(self, mock_file):
        """
        When log_event is called
        Then a log entry should be written
        """
        log_event("TEST LOG")
        mock_file.assert_called()

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_products_execution(self, mock_file):
        """
        When load_products is called
        Then an empty list should be returned
        """
        products = load_products()
        self.assertEqual(products, [])

    @patch("builtins.open", new_callable=mock_open)
    def test_save_products_execution(self, mock_file):
        """
        When save_products is called
        Then products should be written to file
        """
        save_products([{"name": "apple", "price": 10, "code": "12345"}])
        mock_file.assert_called()


if __name__ == "__main__":
    unittest.main()
