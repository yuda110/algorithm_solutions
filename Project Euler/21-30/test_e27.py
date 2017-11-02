import unittest
import cProfile
import e27

class TestSplitFunction(unittest.TestCase) :
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_eular_function(self) :
        r = e27.is_eular_functionable(40)
        self.assertTrue(r)
        r = e27.is_eular_functionable(41)
        self.assertFalse(r)

    def test_is_prime_num(self):
        r = e27.is_prime_num(1)
        self.assertFalse(r)
        r = e27.is_prime_num(0)
        self.assertFalse(r)
        r = e27.is_prime_num(-1)
        self.assertFalse(r)
        r = e27.is_prime_num(2)
        self.assertTrue(r)
        r = e27.is_prime_num(3)
        self.assertTrue(r)
        r = e27.is_prime_num(17)
        self.assertTrue(r)
        r = e27.is_prime_num(23)
        self.assertTrue(r)

    def test_is_eular_2cha(self):
        r = e27.is_eular_2cha(40)
        self.assertTrue(r)
        r = e27.is_eular_2cha(41)
        self.assertFalse(r)
        r = e27.is_eular_2cha(41,-1,41)
        self.assertTrue(r)
        r = e27.is_eular_2cha(79,-77,1523)
        self.assertTrue(r)

    def test_get_euler_a_b(self):
        r = e27.get_euler_a_b(2, 42)
        self.assertEqual(r,(-1,41))
        #r = e27.get_euler_a_b(1000, 1000)

if __name__ == '__main__':
    unittest.main()
    #cProfile.run('e27.get_euler_a_b(1000, 1000)')