class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i=0
        N=len(arr)
        while i<N-1 and arr[i]<arr[i+1]:
            i=i+1
        if i == 0 or i == N - 1:
            return False
        while i<N-1 and arr[i]>arr[i+1]:
            i=i+1
        
        return i==N-1
