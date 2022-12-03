"""
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""
class Solution(object):
    def arrangeCoins(self, coins):
        """
        :type n: int
        :rtype: int
        """
        steps = 0

        while steps <= coins:
            coins -= steps
            steps += 1

        return steps - 1

test = Solution()
print(test.arrangeCoins(20))

"""
There is an alternative math solution with the quadratic formula.
 return int((-1 + (1 + 8*coins) ** 0.5) // 2)
"""