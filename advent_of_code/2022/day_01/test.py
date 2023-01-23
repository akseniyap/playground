import unittest
from solution import easy, hard, get_data
from utils.py_utils.constants import SAMPLE


class Day01(unittest.TestCase):
    def setUp(self):
        self.data = get_data(SAMPLE)

    def test_easy(self):
        result = easy(self.data)
        self.assertEqual(result, 24_000)

    def test_hard(self):
        result = hard(self.data)
        self.assertEqual(result, 45_000)


if __name__ == "__main__":
    unittest.main()
