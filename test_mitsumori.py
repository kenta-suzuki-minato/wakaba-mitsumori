import unittest

from mitsumori import zeikomi


class TestZeikomi(unittest.TestCase):
    def test_round_number(self):
        self.assertEqual(zeikomi(1000), 1100)

    def test_floor_fraction(self):
        # 1236円 x 1.1 = 1359.6円 -> 1円未満切り捨てで1359円
        self.assertEqual(zeikomi(1236), 1359)


if __name__ == "__main__":
    unittest.main()
