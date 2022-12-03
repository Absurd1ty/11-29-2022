"""
Given two non-negative integers, num1 and num2 represented as
string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for
handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1)
        num2 = list(num2)
        carryover = 0
        result = ""
        while num1 or num2 or carryover:
            if num1:
                carryover += int(num1.pop())
            print(carryover)
            if num2:
                carryover += int(num2.pop())
            print(carryover)
            result += str((carryover % 10))
            carryover //= 10
        return result[::-1]

test = Solution()
print(test.addStrings("456", "777"))
