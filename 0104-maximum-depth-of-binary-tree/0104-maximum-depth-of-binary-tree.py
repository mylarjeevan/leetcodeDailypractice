# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,height):
            if not node:
                return 0
            height+=1
            if not node.left and not node.right:
                return height
            return max(dfs(node.left,height),dfs(node.right,height))
        return dfs(root,0)

            

        