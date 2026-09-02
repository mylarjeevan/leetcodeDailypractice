class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None
        """

        rows = len(board)
        columns = len(board[0])

        def neighbour(r, c):
            nei = 0

            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):

                    # Skip the cell itself
                    if i == r and j == c:
                        continue

                    # Check boundaries
                    if i < 0 or j < 0 or i >= rows or j >= columns:
                        continue

                    # 1 and 3 were originally alive
                    if board[i][j] == 1 or board[i][j] == 3:
                        nei += 1

            return nei

        # First pass: mark temporary states
        for r in range(rows):
            for c in range(columns):

                nei = neighbour(r, c)

                # Cell is currently alive
                if board[r][c] == 1:

                    if nei == 2 or nei == 3:
                        board[r][c] = 3  # alive -> alive

                    # Otherwise it remains 1 for now
                    # and will become 0 in second pass

                # Cell is currently dead
                elif board[r][c] == 0:

                    if nei == 3:
                        board[r][c] = 2  # dead -> alive

        # Second pass: convert temporary states
        for r in range(rows):
            for c in range(columns):

                if board[r][c] == 1:
                    board[r][c] = 0

                elif board[r][c] == 2 or board[r][c] == 3:
                    board[r][c] = 1