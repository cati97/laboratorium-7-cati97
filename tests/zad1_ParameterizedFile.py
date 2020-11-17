import unittest
from src.sample.zad1 import *


class HammingParameterizedFile(unittest.TestCase):
    def setUp(self):
        self.hamming = Hamming()

    def test_from_data_file(self):
        with open("data/zad1_data_tests") as file_tests:
            for line in file_tests:
                if line.startswith("#") or line.startswith("\n"):
                    continue
                else:
                    data = line.split(',')
                    str1, str2, expected = data[0], data[1], int(data[2].strip('\n'))
                    self.assertEqual(self.hamming.distance(str1, str2), expected)

    def test_exceptions_from_data_file(self):
        with open("data/zad1_data_exceptions") as file_exceptions:
            for line in file_exceptions:
                if line.startswith("#"):
                    continue
                else:
                    data = line.split(',')
                    str1, str2 = data[0], data[1]
                    self.assertRaises(ValueError, self.hamming.distance, str1, str2)


if __name__ == '__main__':
    unittest.main()


# to work from here - change paths add ../
# to work from lab7 in terminal using coverage run --source=src/ setup.py test path - data/zad1_data_exceptions
