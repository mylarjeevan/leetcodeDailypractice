class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        for i in range(1,len(nums)):
            while nums[i-1]!=nums[i]-1:
                ans.append(nums[i-1]+1)
                nums[i-1]+=1
        return ans


