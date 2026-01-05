import unittest
from security import validate_card_number, validate_cvv, validate_expiry

class TestSecurityWhiteBox(unittest.TestCase):

    def test_valid_card_number(self):
        self.assertTrue(validate_card_number("1234567812345678"))

    def test_invalid_card_number(self):
        self.assertFalse(validate_card_number("1234"))

    def test_valid_cvv(self):
        self.assertTrue(validate_cvv("123"))

    def test_invalid_cvv(self):
        self.assertFalse(validate_cvv("12"))

    def test_valid_expiry(self):
        self.assertTrue(validate_expiry("12/30"))

    def test_invalid_expiry(self):
        self.assertFalse(validate_expiry("13/10"))

if __name__ == "__main__":
    unittest.main()
