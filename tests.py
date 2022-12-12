import unittest
from calculator import prime_calculator


class TesCalculator(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(prime_calculator(3, '+', 2), 5)
        self.assertEqual(prime_calculator(10.5, '-', 4.8), 5.7)
        self.assertEqual(prime_calculator(8, '*', 9), 72)
        self.assertEqual(prime_calculator(28, '/', 7), 4)
    def test_operator(self):
        self.assertRaises(ValueError, prime_calculator, 28, '[', 7)
    def test_types(self):
        self.assertRaises(TypeError, prime_calculator, [2], '+', 1)
