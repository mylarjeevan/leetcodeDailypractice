class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans