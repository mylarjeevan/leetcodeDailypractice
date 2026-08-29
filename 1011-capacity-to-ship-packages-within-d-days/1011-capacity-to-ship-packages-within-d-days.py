class Solution(object):
    def shipWithinDays(self, arr, k):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        # code here
        n = len(arr)
        if k > n:
            return -1
        left=max(arr)
        right=sum(arr)
        ans=right
        
        def finder(arr,pages):
            st=1
            pagesstudent=0
            for i in range(len(arr)):
                if(pagesstudent+arr[i]<=pages):
                    pagesstudent+=arr[i]
                else:
                    st+=1
                    pagesstudent=arr[i]
            return st
            
        while left<=right:
            mid=left+(right-left)//2
            if finder(arr,mid)>k:
                left=mid+1
            else:
                ans=min(ans,mid)
                right=mid-1
        return ans
            
            

        