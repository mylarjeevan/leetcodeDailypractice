class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] == 1:      # obstacle
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                if i > 0:
                    dp[i][j] += dp[i-1][j]

                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
                