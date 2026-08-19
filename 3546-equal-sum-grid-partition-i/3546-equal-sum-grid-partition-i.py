class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n=len(grid)
        m=len(grid[0])
        ls=[]
        
        for i in range(n):
            sums=0
            for j in range(m):
                sums+=grid[i][j]
            ls.append(sums)
        val=sum(ls)
        if val % 2 != 0:
            return False
        new=0
        for i in range(len(ls)):
            new+=ls[i]
            if new==val//2:
                return True
        ls=[0]*m
        for j in range(m):
            sums=0
            for i in range(n):
                sums+=grid[i][j]
            ls.append(sums)
        val=sum(ls)
        new=0
        for i in range(len(ls)):
            new+=ls[i]
            if new==val//2:
                return True
        return False

