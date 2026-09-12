class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by ending time
        arr.sort(key=lambda x: x[1])

        # Store ending times for binary search
        ends = [x[1] for x in arr]

        # prev[i] = number of intervals before i
        # whose end < arr[i][0]
        prev = [0] * n

        import bisect

        for i in range(n):
            start = arr[i][0]
            prev[i] = bisect.bisect_left(ends, start, 0, i)

        # dp[i][k] = (maximum score, selected indices)
        #
        # first i intervals considered
        # choose at most k intervals
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher score is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # If score is same, lexicographically smaller
            # sorted list of indices is better
            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            l, r, w, idx = arr[i - 1]

            for k in range(1, 5):

                # Option 1: Don't take current interval
                skip = dp[i - 1][k]

                # Option 2: Take current interval
                old_score, old_indices = dp[prev[i - 1]][k - 1]

                take = (
                    old_score + w,
                    sorted(old_indices + [idx])
                )

                dp[i][k] = better(skip, take)

        return dp[n][4][1]