class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        val=0
        for i in range(len(nums)):
            if bin(i).count('1')==k:
                val+=nums[i]
        return val
        