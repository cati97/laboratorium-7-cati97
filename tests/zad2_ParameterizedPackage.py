import unittest
from src.sample.zad2 import *
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class


@parameterized([
    (1, 'I'),
    (2, 'II'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (6, 'VI'),
    (9, 'IX'),
    (10, 'X'),
])
def test_first_method(input, expected):
    assert_equal(roman(input), expected)


class RomanParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("small", 27, 'XXVII'),
        ("medium", 163, 'CLXIII'),
        ("large", 911, 'CMXI'),
    ])
    def test_floor(self, name, input, expected):
        self.assertEqual(roman(input), expected)


@parameterized_class(('number', 'expected'), [
    (48, "XLVIII"),
    (49, "XLIX"),
    (59, "LIX"),
    (93, "XCIII"),
    (141, "CXLI"),
    (402, "CDII"),
    (575, "DLXXV"),
    (1024, "MXXIV"),
    (3000, "MMM"),
])
class RomanParameterizedPackage2(unittest.TestCase):
    def test_other_parameterized(self):
        self.assertEqual(roman(self.number), self.expected)


if __name__ == '__main__':
    unittest.main()

