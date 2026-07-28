'''class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numed=sorted(nums[:3],reverse=True)
        first=numed[0]
        second=numed[1]
        third=numed[2]
        for i in range(3,len(nums)):
            if nums[i]>=first:
                third=second
                second=first
                first=nums[i]
            elif nums[i]<first and nums[i]>=second:
                third=second
                second=nums[i]
            elif nums[i]<second and nums[i]>third:
                third=nums[i]
        return first*second*third
        
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort(reverse=True)
        val1=nums[0]*nums[1]*nums[2]
        val2=nums[0]*nums[n-1]*nums[n-2]
        return max(val1,val2)
        