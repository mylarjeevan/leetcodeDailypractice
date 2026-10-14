
class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        ans = "9" * (sum // 9)
        rem = sum % 9

        if rem > 0:
            ans += str(rem)

        ans += "0" * (num - len(ans))

        return ans
