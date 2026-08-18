class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n=len(mat)
        m=len(mat[0])
        idx=0
        max_1=0
        
        for i in range(n):
            count=0
            for j in range(m):
                if mat[i][j]==1:
                    count+=1
            if count>max_1:
                max_1=count
                idx=i
        return [idx,max_1]
            
        