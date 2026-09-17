class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        best = INF
        ans = INF
        left = 0
        curr = 0

        # best[i] = minimum valid subarray length ending at or before i
        best = [INF] * n

        for right in range(n):
            curr += arr[right]

            while curr > target and left <= right:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1

                # Previous non-overlapping subarray must end before left
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                # Store the best single subarray
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)
            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == INF else ans