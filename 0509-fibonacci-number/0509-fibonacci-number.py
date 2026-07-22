class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        prev2=0
        prev1=1
        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1
        