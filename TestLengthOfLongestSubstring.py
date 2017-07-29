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

    def test_stringOfDigits(self):
        '''Testing for string containing digits'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("1231244"), 3)

    def test_UpperCaseChars(self):
        '''Testing for string containing uppercase characters'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("ABCDAB"), 4)
        self.assertEqual(obj.lengthOfLongestSubstring("AbcdAB"), 4)

    def test_specialChars(self):
        '''Testing for string containing special characters'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring("@@@@"), 1)
        self.assertEqual(obj.lengthOfLongestSubstring("@@@@abc"), 4)

    def test_emptyString(self):
        '''Testing for empty string'''
        obj = Solution()
        self.assertEqual(obj.lengthOfLongestSubstring(""), 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
