class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs)
        n=len(nums)
        if n==1:
            return nums[0]**2
        val=0
        val-=nums[0]**2
        for i in range(1,n//2):
            val-=nums[i]**2
        for i in range(n//2,n,1):
            val+=nums[i]**2
        return val

