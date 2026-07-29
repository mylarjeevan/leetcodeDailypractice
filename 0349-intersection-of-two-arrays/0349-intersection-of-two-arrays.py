class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        l1=[]
        for i in nums1:
            if i in nums2:
                l1.append(i)
        return l1