import unittest
from LengthOfLongestSubstring import Solution

class TestCases(unittest.TestCase):
    def test_multipleLongest(self):
        '''Testing for abcabcbb'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_allRepeatedChars(self):
        '''Testing for bbbbb'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("bbbbb"), 1)

    def test_someRepeatedChars(self):
        '''Testing for pwwkew'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("pwwkew"), 3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
