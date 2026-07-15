class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        prev2=nums[0]
        prev1=max(prev2,nums[1])
        for i in range(2,n):
            pick=nums[i]+prev2
            not_pick=prev1
            curr=max(pick,not_pick)
            prev2=prev1
            prev1=curr
        return prev1
        