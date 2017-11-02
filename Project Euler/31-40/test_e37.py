import e37
import unittest

class TestSplitFunction(unittest.TestCase):
    def test_is_prime(self):
        r = e37.is_prime(3797)
        self.assertTrue(r)
        r = e37.is_prime(24)
        self.assertFalse(r)

    def test_is_still_prime(self):
        r = e37.is_still_prime(3797)
        self.assertTrue(r)
        r = e37.is_still_prime(222)
        self.assertFalse(r)

if __name__ == '__main__':
    unittest.main()