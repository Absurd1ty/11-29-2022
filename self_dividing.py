class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def divisible(n):
            for num in str(n):
                if num == '0' or n % int(num) > 0:
                    return False
            return True

        res = []
        for num in range(left, right + 1):
            if divisible(num):
                res.append(num)
        return res


test = Solution()
print(test.selfDividingNumbers(1, 22))