"""Tests for every calculator operation and its boundary cases."""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src/main/python"))

from calculator_AliRida_Awad import (  # noqa: E402
    add, subtract, multiply, divide, modulus, power, square_root,
)


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-2, 2), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 2), 0)
        self.assertEqual(modulus(-10, 3), 2)
        self.assertAlmostEqual(modulus(5.5, 2), 1.5)

    def test_modulus_by_zero(self):
        with self.assertRaisesRegex(ValueError, "zero divisor"):
            modulus(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(-2, 3), -8)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)

    def test_square_root_negative(self):
        with self.assertRaisesRegex(ValueError, "negative number"):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
