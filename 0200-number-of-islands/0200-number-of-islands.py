
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]

        def dfs(row, col):
            vis[row][col] = 1

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if (0 <= nr < n and 0 <= nc < m
                    and grid[nr][nc] == '1'
                    and not vis[nr][nc]):
                    dfs(nr, nc)

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not vis[i][j]:
                    count += 1
                    dfs(i, j)

        return count