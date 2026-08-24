class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        # Search
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found node
        else:
            # 0 or 1 child
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            # 2 children
            temp = root.left

            # Find rightmost node in left subtree
            while temp.right:
                temp = temp.right

            # Attach right subtree
            temp.right = root.right

            return root.left

        return root