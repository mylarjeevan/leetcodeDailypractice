class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)

        if k == 1:
            mp = {}

            for x in nums:
                mp[x] = mp.get(x, 0) + 1

            ans = -1

            for x in mp:
                if mp[x] == 1:
                    ans = max(ans, x)

            return ans

        if k == n:
            return max(nums)

        mp = {}

        for i in range(n - k + 1):
            for j in range(i, i + k):
                mp[nums[j]] = mp.get(nums[j], 0) + 1

        ans = -1

        for x in mp:
            if mp[x] == 1:
                ans = max(ans, x)

        return ans