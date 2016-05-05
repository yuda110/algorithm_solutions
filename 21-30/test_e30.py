import e30
import unittest
import cProfile

class TestSplitFunction(unittest.TestCase) :
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_cal_pound(self):
        r = e30.is_square_five()
        self.assertEqual(r, 443839)


if __name__ == '__main__':
    unittest.main()