class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        first_row = any(matrix[0][j] == 0 for j in range(m))
        first_col = any(matrix[i][0] == 0 for i in range(n))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row:
            for j in range(m):
                matrix[0][j] = 0

        if first_col:
            for i in range(n):
                matrix[i][0] = 0