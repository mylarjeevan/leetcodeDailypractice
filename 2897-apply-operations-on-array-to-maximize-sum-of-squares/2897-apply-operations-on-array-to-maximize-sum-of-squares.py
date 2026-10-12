
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 31

        # Count set bits at every position
        for num in nums:
            for i in range(31):
                if num & (1 << i):
                    cnt[i] += 1

        ans = 0

        # Construct the largest possible k numbers
        for _ in range(k):
            x = 0

            for i in range(31):
                if cnt[i] > 0:
                    x |= (1 << i)
                    cnt[i] -= 1

            ans = (ans + x * x) % MOD

        return ans
