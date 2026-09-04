class Solution(object):
    def minDays(self, bloomDay, m, k):

        n = len(bloomDay)

        # Impossible case
        if m * k > n:
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:

            mid = (low + high) // 2

            # Check whether mid days are enough
            bouquets = 0
            flowers = 0

            for day in bloomDay:

                if day <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            # Binary search
            if bouquets >= m:
                high = mid - 1
            else:
                low = mid + 1

        return low