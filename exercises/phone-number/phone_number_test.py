import unittest

from phone_number import Phone


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class PhoneTest(unittest.TestCase):
    def test_cleans_number(self):
        number = Phone("(223) 456-7890").number
        self.assertEqual(number, "2234567890")

    def test_cleans_number_with_dots(self):
        number = Phone("223.456.7890").number
        self.assertEqual(number, "2234567890")

    def test_cleans_number_with_multiple_spaces(self):
        number = Phone("223 456   7890   ").number
        self.assertEqual(number, "2234567890")

    def test_invalid_when_9_digits(self):
        number = Phone("123456789").number
        self.assertEqual(number, "0000000000")

    def test_invalid_when_11_digits_and_first_not_1(self):
        number = Phone("22234567890").number
        self.assertEqual(number, "0000000000")

    def test_valid_when_11_digits_and_first_is_1(self):
        number = Phone("12234567890").number
        self.assertEqual(number, "2234567890")

    def test_valid_when_11_digits_and_first_is_1_with_punctuation(self):
        number = Phone("+1 (223) 456-7890").number
        self.assertEqual(number, "2234567890")

    def test_invalid_when_more_than_11_digits(self):
        number = Phone("321234567890").number
        self.assertEqual(number, "0000000000")

    def test_invalid_with_letters(self):
        number = Phone("123-abc-7890").number
        self.assertEqual(number, "0000000000")

    def test_invalid_with_punctuation(self):
        number = Phone("123-@:!-7890").number
        self.assertEqual(number, "0000000000")

    def test_invalid_area_code(self):
        number = Phone("(123) 456-7890").number
        self.assertEqual(number, "0000000000")

    def test_invalid_exchange_code(self):
        number = Phone("(223) 056-7890").number
        self.assertEqual(number, "0000000000")

    # Track specific tests
    def test_area_code(self):
        number = Phone("2234567890")
        self.assertEqual(number.area_code(), "223")

    def test_pretty_print(self):
        number = Phone("2234567890")
        self.assertEqual(number.pretty(), "(223) 456-7890")

    def test_pretty_print_with_full_us_phone_number(self):
        number = Phone("12234567890")
        self.assertEqual(number.pretty(), "(223) 456-7890")


if __name__ == '__main__':
    unittest.main()
