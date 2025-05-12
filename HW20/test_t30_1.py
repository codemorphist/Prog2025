import unittest
from random import choice, uniform

from t30_1 import *


class TestTaylorSum(unittest.TestCase):
    def test_known_values(self):
        self.assertAlmostEqual(taylor(0.0), 1.0, places=6)
        self.assertAlmostEqual(taylor(0.5), 1 / (1 + 0.5)**2, places=4)
        self.assertAlmostEqual(taylor(-0.5, 10e-8), 1 / (1 - 0.5)**2, places=4)

    def test_convergence_precision(self):
        value1 = taylor(0.5, eps=1e-3)
        value2 = taylor(0.5, eps=1e-8)
        self.assertAlmostEqual(value1, value2, places=2)  
        self.assertAlmostEqual(value2, 1 / (1.5**2), places=6)

    def test_out_of_domain(self):
        with self.assertRaises(ValueError):
            taylor(1.0)

        with self.assertRaises(ValueError):
            taylor(-1.5)


if __name__ == "__main__":
    unittest.main()
