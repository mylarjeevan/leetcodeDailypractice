class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for i,x in enumerate(nums):
            if freq[x]>len(nums)//2:
                return x 
        