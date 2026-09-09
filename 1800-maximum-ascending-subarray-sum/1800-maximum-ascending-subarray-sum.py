class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count=nums[0]
        ans=nums[0]
        i=1
        while i<len(nums):
            if nums[i]>nums[i-1]:
                count+=nums[i]
                i+=1
            else:
                count=nums[i]
                i+=1
            ans=max(ans,count)
            
        
            
        return ans
            
            

        