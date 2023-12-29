import unittest

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

class TestFactorialRecursive(unittest.TestCase):

    def test_factorial_of_zero(self):
        result = factorial_recursive(0)
        self.assertEqual(result, 1)

    def test_factorial_of_one(self):
        result = factorial_recursive(1)
        self.assertEqual(result, 1)

    def test_factorial_of_positive_number(self):
        result = factorial_recursive(5)
        self.assertEqual(result, 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-3)

if __name__ == '__main__':
    unittest.main()
