'''
Word Break
Given an input string and a dictionary of words,
find out if the input string can be segmented into a space-separated sequence of dictionary words.
For example, consider the following dictionary:
{ pear, salmon, foot, prints, footprints, leave, you, sun, girl, enjoy },
Examples:Given the string “youenjoy”, 
Output: True (The string can be segmented as “you enjoy”)
Input: “youleavefootprints”,
Output: True (The string can be segmented as “you leave footprints” or “you leave foot prints”)
Input:salmonenjoyapples
Output: False
'''
class Solution():
    def wordBreak(self, s, dictionary):
        if s == "" or dictionary == {}:
            return False
        s = s.lower()
        for word in dictionary:
            word = word.lower()
            if word in s:
                s = s.replace(word,"")
            if s == "":
                return True
        return s == ""
        
if __name__ == '__main__':
    obj = Solution()
