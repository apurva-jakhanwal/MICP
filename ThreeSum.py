'''
3Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
'''

class Solution():
    def threeSum(self, arr):
        if len(arr) < 3 or arr == []:
            return []
        arrOfArr = []
        for i in range(0, len(arr)):
            if (i+1) < len(arr):
                if (-(arr[i] + arr[i+1])) in arr:
                    subArr=[arr[i], arr[i+1], -(arr[i] + arr[i+1])]
                    if sorted(subArr) not in arrOfArr:
                        arrOfArr.append(sorted(subArr))
        return arrOfArr


if __name__ == '__main__':
    obj = Solution()
    print(obj.threeSum([]))
    print(obj.threeSum([1,2,3,4,5,6]))
    print(obj.threeSum([-1,0,1]))
    print(obj.threeSum([0,1]))
    print(obj.threeSum([0,0,0]))
    print(obj.threeSum([-1,0,1,2,-1,4]))
  
    
