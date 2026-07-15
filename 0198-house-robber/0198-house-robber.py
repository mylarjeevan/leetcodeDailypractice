class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        dp={}
        def func(nums,n):
        
            if n==0:
                return nums[n]
            if n<0:
                return 0
            if n in dp:
                return dp[n]
            pick=nums[n]+func(nums,n-2)
            not_pick=0+func(nums,n-1)
            dp[n]=max(pick,not_pick)
            return dp[n]

        return func(nums,size-1)