class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        freq={}
        count=0
        for x in stones:
            freq[x]=freq.get(x,0)+1
        for i in range(len(jewels)):
            count+=freq.get(jewels[i],0)
        return count