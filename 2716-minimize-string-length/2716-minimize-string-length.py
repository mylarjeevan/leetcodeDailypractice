class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        v=set()
        for i in range(len(s)):
            v.add(s[i])
        return len(v)
        