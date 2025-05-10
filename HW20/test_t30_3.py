import unittest

from t30_3 import *


class TestHammingDist(unittest.TestCase):
    def test_equal_strings(self):
        self.assertEqual(hamming_dist("abcd", "abcd"), 0)

    def test_some_differences(self):
        self.assertEqual(hamming_dist("abcd", "abcf"), 1)
        self.assertEqual(hamming_dist("10101", "11100"), 2)
        self.assertEqual(hamming_dist("karolin", "kathrin"), 3)
        self.assertEqual(hamming_dist("2173896", "2233796"), 3)

    def test_all_different(self):
        self.assertEqual(hamming_dist("aaaa", "bbbb"), 4)

    def test_empty_strings(self):
        self.assertEqual(hamming_dist("", ""), 0)

    def test_unequal_length(self):
        with self.assertRaises(ValueError):
            hamming_dist("abc", "ab")


if __name__ == "__main__":
    unittest.main()
