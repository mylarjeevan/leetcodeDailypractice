class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_min=0
        left_max=0
        for i in range(len(s)):
            if s[i]=='(':
                left_min+=1
                left_max+=1
            elif s[i]=='*':
                left_min-=1
                left_max+=1
            else:
                left_min-=1
                left_max-=1
            if left_max<0:
                return False
            if left_min<0:
                left_min=0
            
        return left_min==0 
            

            
        