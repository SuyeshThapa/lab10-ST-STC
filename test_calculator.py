# https://github.com/SuyeshThapa/lab10-ST-STC.git
# Partner 1: Suyesh Thapa
# Partner 2: Suyesh Thapa Clone

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1021, 19), 1040)
        self.assertEqual(add(-17, -23), -40)
        self.assertEqual(add(5.5, -30), -24.5)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(-23, -3), -20)
        self.assertEqual(subtract(5, -1000), 1005)
        self.assertEqual(subtract(15.75, 5), 10.75)

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(0, 100), 0)
        self.assertEqual(mul(-3, -10), 30)
        self.assertEqual(mul(-10.5, 1000), -10500)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(-50, 1000), -20)
        self.assertAlmostEqual(div(7, 22), 22 / 7)
        self.assertEqual(div(10, -2), -0.2)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # Call division function inside. Example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
            div(0, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 32), 5)
        self.assertEqual(logarithm(109, 1), 0)
        self.assertEqual(logarithm(2.5, 6.25), 2)

    def test_log_invalid_base(self):  # 1 assertion
        # Use same technique from test_divide_by_zero.
        with self.assertRaises(ValueError):
            logarithm(10, -1)
            logarithm(32, 0)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # Call log function inside. Example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)
            logarithm(-2, 2)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-12, -5), 13)
        self.assertAlmostEqual(hypotenuse(2.5, 2.5), (2.5 ** 2 + 2.5 ** 2) ** (1 / 2))

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument. Example:
        with self.assertRaises(ValueError):
            square_root(-36)
            square_root(-101.75)

        # Test basic function.
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(2500), 50)
        self.assertAlmostEqual(square_root(3), 3 ** (1 / 2))

# Do not touch this.
if __name__ == "__main__":
    unittest.main()