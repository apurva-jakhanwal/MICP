'''
Given a string, find the length of the longest substring without repeating characters.
'''
class Solution():
    def lengthOfLongestSubstring(self, s):
        res = ""
        result = []
        for i in range(0, len(s)):
            if s[i] not in res:
                res += s[i]
            else:
                result.append(res)
                res = ""
                res += s[i]
        max = 0
        for val in result:
            if len(val) > max:
                max = len(val)
        return max


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring("abcabcbb"))
    print(obj.lengthOfLongestSubstring("bbbbb"))
    print(obj.lengthOfLongestSubstring("pwwkew"))
    
