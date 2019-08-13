import unittest
import time

from burn import fib

class TestFib(unittest.TestCase):
    def test_fib(self):
        """
        Test fib()
        """
        self.assertEqual(fib(0), 1)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 8)

    def test_slowness(self):
        """
        Verify fib() is super slow
        """
        start = time.time()
        _ = fib(25)
        end = time.time()
        self.assertGreater(end - start, 1e-3)

if __name__ == '__main__':
    unittest.main()
