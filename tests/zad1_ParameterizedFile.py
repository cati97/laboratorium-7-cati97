import unittest
from src.sample.zad1 import *


class HammingParameterizedFile(unittest.TestCase):
    def setUp(self):
        self.hamming = Hamming()

    def test_from_data_file(self):
        with open("../data/zad1_data_tests") as file_tests:
            for line in file_tests:
                if line.startswith("#") or line.startswith("\n"):
                    continue
                else:
                    data = line.split(',')
                    str1, str2, expected = str(data[0]), str(data[1]), int(data[2].strip('\n'))
                    self.assertEqual(self.hamming.distance(str1, str2), expected)


if __name__ == '__main__':
    unittest.main()
