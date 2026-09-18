from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)
        full = (1 << k) - 1

        # best[r][c][mask] = maximum energy seen at this state
        best = [[[ -1] * (1 << k) for _ in range(n)] for _ in range(m)]

        q = deque([(sr, sc, energy, 0)])
        best[sr][sc][0] = energy

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == full:
                    return moves

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if classroom[nr][nc] == 'X':
                        continue
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if (nr, nc) in litter:
                        nmask |= 1 << litter[(nr, nc)]

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Dominance pruning
                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne
                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1