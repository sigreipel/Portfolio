import unittest
from RomanNumerals.Roman_Numerals import RomanNumeralConversion


class RomanNumeralTest(unittest.TestCase):
    # Tests for Roman Numeral conversion
    def test_convert_rm_zero(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, 0)

    def test_convert_rm_negative(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, -1)

    def test_convert_rm_string(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, "cheese")

    def test_convert_rm_4000(self):    # throwing an error because I have not implemented this
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, 4000)

    # Tests for integer conversion
    def test_convert_int_string(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, "20")

    def test_convert_int_string2(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, "20abc")

    def test_convert_int_invalid(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, "IIII")

    def test_convert_int_invalid2(self):
        self.assertRaises(Exception, RomanNumeralConversion.convertToRomanNumeral, "LXIIII")

if __name__ == 'main':
    unittest.main()
