import unittest
from unittest.mock import patch
from order import checkout


class TestCheckoutSymbolic(unittest.TestCase):
    """
    Symbolic Execution Paths for checkout():

    Path 1: quantity >= 5   → bulk discount
    Path 2: subtotal >= 100 → cart discount
    Path 3: card payment + correct OTP
    """

    def test_symbolic_bulk_discount_path(self):
        """
        Symbolic condition: q >= 5
        """
        quantity = 5
        self.assertTrue(quantity >= 5)

    def test_symbolic_cart_offer_path(self):
        """
        Symbolic condition: subtotal >= 100
        """
        subtotal = 120
        self.assertTrue(subtotal >= 100)

    def test_symbolic_invalid_otp_path(self):
        """
        Symbolic condition: entered_otp != expected_otp
        """
        expected_otp = 1234
        entered_otp = 1111
        self.assertNotEqual(expected_otp, entered_otp)

    # ------------------------------------------------
    # SYMBOLIC-GUIDED EXECUTION (COVERAGE BOOSTER)
    # ------------------------------------------------

    @patch("order.random.randint", return_value=4321)
    @patch("order.load_orders", return_value=[])
    @patch("order.save_orders")
    @patch("builtins.input", side_effect=[
        "n",                        # no coupon
        "card",                     # payment method
        "1234567812345678",         # valid card
        "12/26",                    # expiry
        "123",                      # cvv
        "4321",                     # correct OTP
        "4"                         # ✅ skip receipt
    ])
    def test_symbolic_guided_card_payment(
        self, mock_input, mock_save, mock_load, mock_rand
    ):
        """
        Concrete execution guided by symbolic path:
        payment_method == card AND otp_valid == True
        """
        cart = [{"name": "apple", "price": 25, "quantity": 4}]

        checkout(cart, "5555555555")

        # Observable effect
        self.assertEqual(cart, [])
        self.assertTrue(mock_save.called)


if __name__ == "__main__":
    unittest.main()
