class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1000:
            return 0
        return (n-1000)+1
        