class Solution(object):
    def maxJump(self, stones):
        ans = stones[1] - stones[0]

        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i-2])

        return ans