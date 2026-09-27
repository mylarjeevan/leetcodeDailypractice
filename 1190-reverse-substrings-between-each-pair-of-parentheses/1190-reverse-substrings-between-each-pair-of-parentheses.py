class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ')':
                temp = []

                # Pop until matching '('
                while stack[-1] != '(':
                    temp.append(stack.pop())

                stack.pop()  # remove '('

                # Put reversed substring back
                stack.extend(temp)

            else:
                stack.append(ch)

        return ''.join(stack)