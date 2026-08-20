class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq1={}
        freq2={}
        for x in ransomNote:
            freq1[x]=freq1.get(x,0)+1
        for y in magazine:
            freq2[y]=freq2.get(y,0)+1
        i=0
        for x in freq1:
            if freq1[x]>freq2.get(x,0):
                return False
        return True

        
        