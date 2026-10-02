class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        freq1={}
        freq2={}
        for x in s:
            freq1[x]=freq1.get(x,0)+1
        for y in t:
            freq2[y]=freq2.get(y,0)+1
        return freq1==freq2
