class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        row=n
        column=n
        matrix=[[0]*column for i in range(row)]
        left=0
        right=n-1
        top=0
        bottom=n-1
        num=1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                matrix[top][i]=num
                num+=1
            top+=1
            for i in range(top,bottom+1):
                matrix[i][right]=num
                num+=1
            right-=1



            for i in range(right,left-1,-1):
                matrix[bottom][i]=num
                num+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                matrix[i][left]=num
                num+=1
            left+=1
        return matrix
            