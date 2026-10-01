class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
        def fun(val):
            count=0
            while val:
                count+=val&1
                val>>=1
            return count
        for i in range(n+1):
            ans.append(fun(i))
        return ans
