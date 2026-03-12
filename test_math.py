import unittest
from main import MathAlgorithms

class TestMathAlgos(unittest.TestCase):
    def test_sieve(self):
        self.assertEqual(MathAlgorithms.sieve_of_eratosthenes(10), [2, 3, 5, 7])

    def test_gcd(self):
        self.assertEqual(MathAlgorithms.gcd_recursive(48, 18), 6)
        self.assertEqual(MathAlgorithms.gcd_iterative(48, 18), 6)

    def test_power(self):
        self.assertAlmostEqual(MathAlgorithms.fast_power(2, 10), 1024)
        self.assertAlmostEqual(MathAlgorithms.fast_power(2, -2), 0.25)

    def test_sqrt(self):
        self.assertEqual(MathAlgorithms.square_root(8), 2)
        self.assertEqual(MathAlgorithms.square_root(16), 4)

    def test_zeroes(self):
        self.assertEqual(MathAlgorithms.trailing_zeroes(5), 1)
        self.assertEqual(MathAlgorithms.trailing_zeroes(100), 24)

if __name__ == '__main__':
    unittest.main()