class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ls = []
        n = len(nums)

        i = 0

        while i < n - 2:


            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = n - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ls.append([nums[i], nums[j], nums[k]])

              
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    k -= 1

            i += 1

        return ls