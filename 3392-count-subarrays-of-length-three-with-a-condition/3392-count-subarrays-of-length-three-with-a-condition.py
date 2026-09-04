
class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=left+2
        count=0
        while right<len(nums):
            if nums[left]+nums[right]==nums[left+1]/2.0:
                count+=1
            left+=1
            right=left+2
        return count


        