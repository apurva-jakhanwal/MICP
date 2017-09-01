import unittest
from BT_subtree import Node, isSubtree

class TestCases(unittest.TestCase):

    def test_singleNodes(self):
        '''When both trees have single nodes'''
        T = Node(1)

        S = Node(1)

        self.assertEqual(isSubtree(T, S), True)

    def test_fullySame(self):
        '''When both trees are the same'''
        T = Node(1)
        T.left = Node(2)
        T.right = Node(3)

        S = Node(1)
        S.left = Node(2)
        S.right = Node(3)

        self.assertEqual(isSubtree(T, S), True)

    def test_subtree(self):
        '''When one tree is a subtree of another'''
        T = Node(1)
        T.left = Node(2)
        T.right = Node(3)
        T.left.left = Node(4)
        T.left.right = Node(5)

        S = Node(2)
        S.left = Node(4)
        S.right = Node(5)

        self.assertEqual(isSubtree(T, S), True)

    def test_simpleFail(self):
        '''Simple Failure in passing the subtree test'''
        T = Node(1)
        T.left = Node(2)
        T.right = Node(3)

        S = Node(1)
        S.left = Node(2)

        self.assertEqual(isSubtree(T, S), False)

    def test_partiallySame(self):
        '''When one tree is not a subtree of another because of a missing leaf'''
        T = Node(1)
        T.left = Node(2)
        T.right = Node(3)
        T.left.left = Node(4)
        T.left.right = Node(5)
        T.left.right.right = Node(6)

        S = Node(2)
        S.left = Node(4)
        S.right = Node(5)

        self.assertEqual(isSubtree(T, S), False)

    def test_alphabets(self):
        '''Trees contain alphabetic characters'''
        T = Node('a')
        T.left = Node('b')
        T.right = Node('c')
        T.left.left = Node('d')
 
        S = Node('a')
        S.left = Node('b')
        S.right = Node('c')
        S.left.left = Node('d')

        self.assertEqual(isSubtree(T, S), True)

    def test_otherChars(self):
        '''Trees contain numbers, alphabets and other special characters'''
        T = Node('$')
        T.left = Node('a')
        T.right = Node('1')
 
        S = Node('$')
        S.left = Node('a')
        S.right = Node('1')

        self.assertEqual(isSubtree(T, S), True)

    def test_caseSensitivity(self):
        '''Upper Case and Lower Case check'''
        T = Node('a')
        T.left = Node('b')
        T.right = Node('c') 

        S = Node('A')
        S.left = Node('b')
        S.right = Node('c')

        self.assertEqual(isSubtree(T, S), False)
            
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
