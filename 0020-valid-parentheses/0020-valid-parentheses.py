class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                st.append(s[i])
            elif len(st)>0 and ((s[i]==")" and st[-1]=="(") or  (s[i]=="]" and st[-1]=="[") or  (s[i]=="}" and st[-1]=="{")):
                st.pop()
            else:
                return False
        if not st:
            return True
        return False
        