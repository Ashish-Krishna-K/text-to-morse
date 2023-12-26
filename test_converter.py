import unittest

from converter import Converter


class TestConverter(unittest.TestCase):
    """Runs all the unit tests"""

    def setUp(self):
        self.converter = Converter()

    def test_converter(self):
        """Tests the convert_text function"""
        result = self.converter.convert_text("Hello")
        self.assertEqual(result, "....   .   .-..   .-..   ---")


if __name__ == "__main__":
    unittest.main()
