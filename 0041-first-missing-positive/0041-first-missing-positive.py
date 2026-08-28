class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        # Put every number x at index x-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1

                nums[i], nums[correct_index] = \
                    nums[correct_index], nums[i]

        # Find first incorrect position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1