class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2

            # Find maximum element in current column
            max_row = 0

            for i in range(n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[max_row][mid + 1] if mid + 1 < m else -1

            # Peak found
            if mat[max_row][mid] > left and mat[max_row][mid] > right:
                return [max_row, mid]

            # Move towards larger neighbor
            elif left > mat[max_row][mid]:
                high = mid - 1

            else:
                low = mid + 1

        return [-1, -1]