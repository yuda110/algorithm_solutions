import e32
import unittest
import cProfile

class TestSplitFunction(unittest.TestCase) :
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_is_pandigital(self):
        r = e32.is_pandigital('39 × 186 = 7254')
        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()