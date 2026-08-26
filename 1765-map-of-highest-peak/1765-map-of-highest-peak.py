from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        q = deque()

        # Water cells have height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))

        # BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n and height[ni][nj] == -1:
                    height[ni][nj] = height[i][j] + 1
                    q.append((ni, nj))

        return height