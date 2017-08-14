import unittest
from WordBreak import Solution

class TestCases(unittest.TestCase):
    def test_emptyString(self):
        '''Testing for empty string'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("", {"summer"}), False)

    def test_emptyDictionary(self):
        '''Testing for empty dictionary'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("summernow", {}), False)

    def test_oneWordSequence(self):
        '''Testing one word sequence'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("hello", {"hello", "world"}), True)

    def test_twoWordsSequence(self):
        '''Testing two words sequence'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("youenjoy", {"pear", "salmon", "foot", "prints", "footprints", "leave", "you", "sun", "girl", "enjoy"}), True)

    def test_moreThan2WordsSequence(self):
        '''Testing more than two words sequence'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("youleavefootprints", {"pear", "salmon", "foot", "prints", "footprints", "leave", "you", "sun", "girl", "enjoy"}), True)

    def test_unsucessfulSequence(self):
        '''Testing unsuccessful sequence'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("salmonenjoyapples", {"pear", "salmon", "foot", "prints", "footprints", "leave", "you", "sun", "girl", "enjoy"}), False)
        self.assertEqual(obj.wordBreak("assomesort", ["some","assort"]), False)
        
    def test_noWordInDictionary(self):
        '''Testing no word in dictionary'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("mycode", {"today"}), False)

    def test_upperCase(self):
        '''Testing upper case in string or words of dictionary'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("Hello", {"hello", "world"}), True)
        self.assertEqual(obj.wordBreak("helloworld", {"Hello", "World"}), True)

    def test_randomCharacters(self):
        '''Testing random characters in string'''
        obj = Solution()
        self.assertEqual(obj.wordBreak("Hello12345$%^", {"hello", "world"}), False)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
