class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(matrix)
        m=len(matrix[0])
        ans=[[0]*n for i in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i]=matrix[i][j]
        return ans