class Solution:
    def bstFromPreorder(self, preorder):
        i = [0]

        def build(bound):

            if i[0] == len(preorder) or preorder[i[0]] > bound:
                return None

            root = TreeNode(preorder[i[0]])
            i[0] += 1

            root.left = build(root.val)
            root.right = build(bound)

            return root

        return build(float('inf'))