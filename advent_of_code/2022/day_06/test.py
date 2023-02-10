import unittest
from solution import easy, hard


class Day06(unittest.TestCase):
    def test_easy_1(self):
        data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        result = easy(data)
        self.assertEqual(result, 7)

    def test_easy_2(self):
        data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        result = easy(data)
        self.assertEqual(result, 5)

    def test_easy_3(self):
        data = "nppdvjthqldpwncqszvftbrmjlhg"
        result = easy(data)
        self.assertEqual(result, 6)

    def test_easy_4(self):
        data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        result = easy(data)
        self.assertEqual(result, 10)

    def test_easy_5(self):
        data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        result = easy(data)
        self.assertEqual(result, 11)

    def test_hard_1(self):
        data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        result = hard(data)
        self.assertEqual(result, 19)

    def test_hard_2(self):
        data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        result = hard(data)
        self.assertEqual(result, 23)

    def test_hard_3(self):
        data = "nppdvjthqldpwncqszvftbrmjlhg"
        result = hard(data)
        self.assertEqual(result, 23)

    def test_hard_4(self):
        data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        result = hard(data)
        self.assertEqual(result, 29)

    def test_hard_5(self):
        data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        result = hard(data)
        self.assertEqual(result, 26)


if __name__ == "__main__":
    unittest.main()
