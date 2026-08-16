class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(code)
        ans=[0]*n
        if k>0:
            for i in range(n):
                val=0
                for j in range(1,k+1):
                    val+=code[(i+j)%n]
                ans[i]=val
            return ans
        if k<0:
            for i in range(n):
                val=0
                for j in range(1,-k+1):
                    val+=code[(i-j)%n]
                ans[i]=val
            return ans
        else:
            return ans
            

