class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1=set(nums1)
        nums2=set(nums2)
        l1=[]
        l2=[]
        answer=[]
        for i in nums1:
            if i not in nums2:
                l1.append(i)
        for i in nums2:
            if i not in nums1:
                l2.append(i)
        answer.append(l1)
        answer.append(l2)
        return answer

        