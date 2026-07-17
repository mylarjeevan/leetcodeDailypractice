class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        new_nums=[0]*n
        for i in range(0,n):
            new_nums[(i+k)%n]=nums[i]
        nums[:]=new_nums
        return nums
        