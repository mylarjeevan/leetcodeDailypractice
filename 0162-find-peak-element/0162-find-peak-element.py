class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                right=mid-1
            elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                return mid
        