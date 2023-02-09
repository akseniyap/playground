import unittest
from solution import easy, hard, get_data
from utils.py_utils.constants import SAMPLE


class Day05(unittest.TestCase):
    def setUp(self):
        self.data = get_data(SAMPLE)

    def test_easy(self):
        result = easy(self.data)
        self.assertEqual(result, "CMZ")

    def test_hard(self):
        result = hard(self.data)
        self.assertEqual(result, "MCD")


if __name__ == "__main__":
    unittest.main()
