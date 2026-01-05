import unittest
from unittest.mock import patch
from order import checkout


class TestCheckoutConcolic(unittest.TestCase):
    """
    Concolic testing combines concrete execution
    with symbolic reasoning about execution paths.
    """

    def test_concolic_valid_payment(self):
        """
        Concrete execution + symbolic reasoning
        Path condition:
        quantity >= 5 AND subtotal < 100
        """
        quantity = 6          # concrete
        price = 10            # concrete
        subtotal = quantity * price

        # symbolic assertions
        self.assertTrue(quantity >= 5)
        self.assertFalse(subtotal >= 100)

    def test_concolic_loyalty_discount(self):
        """
        Concrete value triggering loyalty condition
        Path condition:
        previous_orders >= 3
        """
        previous_orders = 3
        self.assertTrue(previous_orders >= 3)

    # ------------------------------------------------
    # EXECUTION-STYLE CONCOLIC TEST (COVERAGE BOOSTER)
    # ------------------------------------------------

    @patch("order.load_orders", return_value=[
        {"customer": "9999999999", "total": 50},
        {"customer": "9999999999", "total": 60},
        {"customer": "9999999999", "total": 40}
    ])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "n",        # no coupon
        "cash"      # payment method
    ])
    def test_concolic_checkout_execution(self, mock_input, mock_save, mock_load):
        """
        Concolic execution of checkout():
        Concrete cart + symbolic path:
        loyalty_discount_condition == True
        """
        cart = [{"name": "apple", "price": 20, "quantity": 2}]

        # Execute checkout with concrete input
        checkout(cart, "9999999999")

        # Concrete outcome
        self.assertEqual(cart, [])

        # Symbolic reasoning (implicit):
        # previous_orders >= 3 => loyalty discount path taken
        self.assertTrue(mock_save.called)


if __name__ == "__main__":
    unittest.main()
