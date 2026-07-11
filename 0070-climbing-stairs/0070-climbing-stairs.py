class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp={}
        def dfs(n):
            if n==0 or n==1:
                return 1
            if n in dp:
                return dp[n]
            dp[n]=dfs(n-1)+dfs(n-2)
            return dp[n]
        return dfs(n)
       
        