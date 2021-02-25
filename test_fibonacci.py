"""Testing using unittest"""
import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci.fib(0), 0)
        self.assertEqual(fibonacci.fib(2), 1)
        self.assertEqual(fibonacci.fib(4), 3)
        self.assertEqual(fibonacci.fib(5), 5)
        self.assertEqual(fibonacci.fib(7), 13)

    def test_factorial(self):
        self.assertEqual(fibonacci.factorial(1), 1)
        self.assertEqual(fibonacci.factorial(3), 6)
        self.assertEqual(fibonacci.factorial(4), 24)
        self.assertEqual(fibonacci.factorial(5), 120)
        self.assertEqual(fibonacci.factorial(6), 720)

if __name__ == '__main__':
    unittest.main(verbosity=3)