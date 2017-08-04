import unittest
from ThreeSum import Solution

class TestCases(unittest.TestCase):
    def test_emptyArr(self):
        '''Testing for empty array'''
        obj = Solution()
        self.assertEqual(obj.threeSum([]), [])

    def test_noSolution(self):
        '''Testing for no solution'''
        obj = Solution()
        self.assertEqual(obj.threeSum([1,2,3,4,5,6]), [])

    def test_oneSolution(self):
        '''Testing for one solution'''
        obj = Solution()
        self.assertEqual(obj.threeSum([-1,0,1]), [[-1,0,1]])

    def test_lengthLessThan3(self):
        '''Testing for input array with length less than three'''
        obj = Solution()
        self.assertEqual(obj.threeSum([0,1]), [])

    def test_allZeros(self):
        '''Testing for input array which has all zeros'''
        obj = Solution()
        self.assertEqual(obj.threeSum([0,0,0]), [[0, 0, 0]])

    def test_multipleSolutions(self):
        '''Testing for multiple solutions'''
        obj = Solution()
        self.assertEqual(obj.threeSum([-1,0,1,2,-1,4]), [[-1, 0, 1], [-1, -1, 2]])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)
