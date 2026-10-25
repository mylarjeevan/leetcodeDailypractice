class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        ans=""
        i=0
        while i<len(s):
            if not stack:
                stack.append(s[i])
            elif stack and stack[-1]==s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
            i+=1
        while stack:
            val=stack.pop(-1)
            ans=ans+val
        return ans[::-1]

        