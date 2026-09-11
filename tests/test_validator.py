import unittest

from src.validator import is_valid_code


class TestValidator(unittest.TestCase):

    def test_valid_minimum(self):
        self.assertTrue(is_valid_code("1111111111111111"))

    def test_valid_large_code(self):
        self.assertTrue(is_valid_code("9999999999999999"))

    def test_below_minimum(self):
        self.assertFalse(is_valid_code("1111111111111110"))

    def test_too_short(self):
        self.assertFalse(is_valid_code("111111111111111"))

    def test_too_long(self):
        self.assertFalse(is_valid_code("11111111111111111"))

    def test_non_numeric(self):
        self.assertFalse(is_valid_code("111111111111111A"))

    def test_empty(self):
        self.assertFalse(is_valid_code(""))


if __name__ == "__main__":
    unittest.main()
