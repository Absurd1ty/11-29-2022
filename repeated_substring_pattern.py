"""
Given a string s, check if it can be
constructed by taking a substring of it and appending multiple copies of the substring together.
"""
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(1, length//2+1):

            subString = s[:i]
            #print(subString)
            if subString*(length//i) == s:
                return True
        return False

test = Solution()
print(test.repeatedSubstringPattern("abcabcabcabc"))