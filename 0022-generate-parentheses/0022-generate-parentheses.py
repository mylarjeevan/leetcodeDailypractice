class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack=[]
        res=[]
        def back_tracking(OpenN,closedN):
            if OpenN==closedN==n:
                res.append("".join(stack))
                return
            if OpenN<n:
                stack.append("(")
                back_tracking(OpenN+1,closedN)
                stack.pop()
            if closedN<OpenN:
                stack.append(")")
                back_tracking(OpenN,closedN+1)
                stack.pop()
        back_tracking(0,0)
        return res
        