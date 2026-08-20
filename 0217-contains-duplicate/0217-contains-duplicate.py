class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq1={}
        for x in nums:
            freq1[x]=freq1.get(x,0)+1
        for x in freq1:
            if freq1.get(x,0)>1:
                return True
        return False
        