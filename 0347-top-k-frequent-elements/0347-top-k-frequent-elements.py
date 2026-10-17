class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        ans=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        ans = sorted(freq, key=lambda x: freq[x], reverse=True)
        return ans[:k]
