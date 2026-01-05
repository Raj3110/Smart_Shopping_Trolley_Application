import unittest
from unittest.mock import patch
from auth import customer_login, admin_login


class TestLoginBlackBox(unittest.TestCase):
    """
    Black-box tests for authentication functionality.
    Covers success/failure paths for both customer and admin logins.
    """

    @patch("auth.generate_otp", return_value=1234)
    @patch("builtins.input", side_effect=["6303156714", "1234"])
    def test_customer_login_success(self, mock_input, mock_otp):
        """
        Given correct contact number and OTP
        When customer logs in
        Then login should succeed and return contact
        """
        result = customer_login()
        self.assertEqual(result, "6303156714")

    @patch("auth.generate_otp", return_value=1234)
    @patch("builtins.input", side_effect=["6303156714", "9999"])
    def test_customer_login_failure(self, mock_input, mock_otp):
        """
        Given incorrect OTP
        When customer logs in
        Then login should fail
        """
        result = customer_login()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["admin", "admin@123"])
    def test_admin_login_success(self, mock_input):
        """
        Given correct admin credentials
        When admin logs in
        Then access should be granted
        """
        result = admin_login()
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["admin", "wrongpass"])
    def test_admin_login_failure(self, mock_input):
        """
        Given incorrect admin credentials
        When admin logs in
        Then access should be denied
        """
        result = admin_login()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
