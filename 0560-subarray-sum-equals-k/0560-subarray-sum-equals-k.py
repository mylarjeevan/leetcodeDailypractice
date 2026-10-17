
class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            count += freq.get(prefix_sum - k, 0)

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
