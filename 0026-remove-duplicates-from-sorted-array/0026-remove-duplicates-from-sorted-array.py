class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len(nums)
        i=1
        while i<len(nums):
            while i<len(nums) and nums[i]==nums[i-1]:
                nums.remove(nums[i])
            i+=1
        return len(nums)