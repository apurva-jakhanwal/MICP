import unittest
from atoi_itoa import atoi_itoa

class Test(unittest.TestCase):

    def test_atoi(self):
        '''Testing for string to int'''
        i=atoi_itoa()
        self.assertEqual(i.atoi("123"), 123)
        self.assertEqual(i.atoi("9999999"), 9999999)
        self.assertEqual(i.atoi("-901324"), -901324)
        self.assertEqual(i.atoi("-1"), -1)

    def test_itoa(self):
        '''Testing for int to string'''
        i=atoi_itoa()
        self.assertEqual(i.itoa(123), "123")
        self.assertEqual(i.itoa(9999999), "9999999")
        self.assertEqual(i.itoa(-901324), "-901324")
        self.assertEqual(i.itoa(-1), "-1")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
