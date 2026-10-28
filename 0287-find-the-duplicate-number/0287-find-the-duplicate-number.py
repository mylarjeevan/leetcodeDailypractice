class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow