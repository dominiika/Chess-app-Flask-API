from converters import convert_to_tuple, convert_from_tuple
import unittest


class ConverterTests(unittest.TestCase):
    def test_convert_to_tuple(self):
        """Test that a square name is converted to tuple"""
        square = convert_to_tuple("a3")
        self.assertEqual(square, (1, 3))

    def test_convert_from_tuple(self):
        """Test that tuple is converted back to the square name"""
        square = convert_from_tuple((1, 3))
        self.assertEqual(square, "a3")


if __name__ == "__main__":
    unittest.main()
