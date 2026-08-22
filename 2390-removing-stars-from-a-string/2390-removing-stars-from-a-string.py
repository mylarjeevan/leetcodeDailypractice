class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        val=""
        for i in range(len(s)):
            if s[i]=="*":
                val=val[:-1]
            else:
                val+=s[i]
        return val
        