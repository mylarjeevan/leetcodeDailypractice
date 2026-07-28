class Solution(object):
    def maximumProduct(self, nums):
        # Three largest numbers
        first = second = third = float('-inf')

        # Two smallest numbers
        small1 = small2 = float('inf')

        for num in nums:

            # Update three largest
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

            # Update two smallest
            if num < small1:
                small2 = small1
                small1 = num
            elif num < small2:
                small2 = num

        return max(first * second * third,
                   first * small1 * small2)