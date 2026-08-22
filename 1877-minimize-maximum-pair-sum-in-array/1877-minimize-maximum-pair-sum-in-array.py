class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left=0
        right=len(nums)-1
        ans=float('-inf')
        while left<right:
            ans=max(ans,nums[left]+nums[right])
            left+=1
            right-=1
        return ans
