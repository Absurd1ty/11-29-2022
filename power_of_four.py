
"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
import math


class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and math.log(n,4).is_integer()

test = Solution()
print(test.isPowerOfFour(16))