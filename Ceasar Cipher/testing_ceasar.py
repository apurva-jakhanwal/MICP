import unittest
from Ceasar import Ceasar

class TestCeasar(unittest.TestCase):

    def test_input(self):
        '''Testing for correct input parsing'''
        c=Ceasar();
        self.assertEqual(c.parseInput("1:some text"), "some text")
        self.assertEqual(c.parseInput("1:12345"), "12345")

    def test_encrypt_positive(self):
        '''Testing for positive shift'''
        c=Ceasar()
        c.n=1
        self.assertEqual(c.encrypt("some text"), "tpnf ufyu")
        self.assertEqual(c.encrypt("12345"), "23456")
        c.n=100
        self.assertEqual(c.encrypt("abc 123"), "wxy 123")
        c.n=600
        self.assertEqual(c.encrypt("zxyfg"), "bzahi")

    def test_encrypt_negative(self):
        '''Testing for negative shift'''
        c=Ceasar()
        c.n=-1
        self.assertEqual(c.encrypt("abc 123"), "zab 012")
        c.n=-90000
        self.assertEqual(c.encrypt("abc 123"), "mno 123")
        c.n=-22
        self.assertEqual(c.encrypt("WHY!"), "ALC!")


    def test_encrypt_lowercase(self):
        '''Testing for lowercase with positive and negative shift'''
        c=Ceasar()
        c.n=-1
        self.assertEqual(c.encrypt("abc 123"), "zab 012")
        c.n=-998899
        self.assertEqual(c.encrypt("zxy 987"), "ust 098")
        c.n=998899
        self.assertEqual(c.encrypt("zxy 987"), "ecd 876")

    def test_encrypt_uppercase(self):
        '''Testing for uppercase with positive and negative shift'''
        c=Ceasar()
        c.n=-1
        self.assertEqual(c.encrypt("ABC 123"), "ZAB 012")
        c.n=-999999
        self.assertEqual(c.encrypt("ZXY 987"), "MKL 098")
        c.n=999999
        self.assertEqual(c.encrypt("ZXY 987"), "MKL 876")

    def test_encrypt_digits(self):
        '''Testing for digits with positive and negative shift'''
        c=Ceasar()
        c.n=-1
        self.assertEqual(c.encrypt("123"), "012")
        c.n=98765
        self.assertEqual(c.encrypt("888"), "333")

    def test_encrypt_otherChars(self):
        '''Testing for special characters with positive and negative shift'''
        c=Ceasar()
        c.n=-1
        self.assertEqual(c.encrypt(" "), " ")
        c.n=-100000
        self.assertEqual(c.encrypt("!@#"), "!@#")

    def test_encrypt_boundaryCases(self):
        '''Testing for boundary cases'''
        c=Ceasar()
        c.n=1000000000
        self.assertEqual(c.encrypt("abc 123"), "mno 123")
        c.n=-1000000000
        self.assertEqual(c.encrypt("ABC 123"), "OPQ 123")

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCeaser)
    unittest.TextTestRunner(verbosity=2).run(suite)
