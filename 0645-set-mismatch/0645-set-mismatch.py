class Solution:
    def findErrorNums(self, nums):
        n = len(nums)

        # Expected sums
        sum_n = n * (n + 1) // 2
        square_sum_n = n * (n + 1) * (2 * n + 1) // 6

        # Actual sums
        sum_nums = 0
        square_sum_nums = 0

        for num in nums:
            sum_nums += num
            square_sum_nums += num * num

        # x - y
        diff = sum_nums - sum_n

        # x^2 - y^2
        square_diff = square_sum_nums - square_sum_n

        # x + y
        sum_xy = square_diff // diff

        # Duplicate x
        duplicate = (diff + sum_xy) // 2

        # Missing y
        missing = (sum_xy - diff) // 2

        return [duplicate, missing]