class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return nums1
        val=m+n
        for i in range(m,len(nums1)):
            nums1[i]=nums2[val-i-1]
        nums1.sort()
        return nums1

        