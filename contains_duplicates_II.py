"""
Given an integer array nums and an integer k,
return true if there are two distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range (len(nums)):
            if nums[i] in dict and  abs(i - dict[nums[i]]) <= k:
                print(i)
                print(dict[nums[3]])
                return True
            dict[nums[i]] = i

        return False


test = Solution()
print(test.containsNearbyDuplicate([1,2,3,1], 3))