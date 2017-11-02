import e29
import unittest
import cProfile

class TestSplitFunction(unittest.TestCase) :
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_get_square_set(self):
        r = e29.get_square_set(5, 5)
        self.assertEqual(r, 15)
        r = e29.get_square_set(100, 100)
        self.assertEqual(r, 9183)


if __name__ == '__main__':
    unittest.main()