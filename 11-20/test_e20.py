import e20
import unittest
import cProfile

class TestSplitFunction(unittest.TestCase) :
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_sum_factorial(self) :
        r = e20.sum_factorial(100)
        self.assertEqual(r, 648)

if __name__ == '__main__':
    unittest.main()