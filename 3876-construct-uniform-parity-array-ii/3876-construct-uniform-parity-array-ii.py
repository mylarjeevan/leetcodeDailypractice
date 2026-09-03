class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        minimal=min(nums1)
        val=minimal%2
        for i in range(len(nums1)):
            if nums1[i]%2!=val:
                new_nums=nums1[i]-minimal
                if new_nums%2!=val:
                    return False
        return True
        